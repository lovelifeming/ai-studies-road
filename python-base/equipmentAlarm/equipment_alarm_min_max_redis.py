# encoding: utf-8
import datetime
import json
import logging
import sys
import threading
import time
from logging.handlers import TimedRotatingFileHandler
from queue import Queue

import psycopg2.extras
import redis
import requests
from influxdb import InfluxDBClient


def getLogger(fileName: str, name='mylogger', level=logging.DEBUG):
    logger1 = logging.getLogger(name)
    logger1.setLevel(level)
    formatter_str = '[%(asctime)s][%(thread)d][%(filename)s][line: %(lineno)d][%(levelname)s] ## %(message)s'
    datefmt = '%Y-%m-%d %H:%M:%S'
    formatter = logging.Formatter(formatter_str, datefmt)

    rf = TimedRotatingFileHandler(filename=fileName, when="midnight", interval=1, backupCount=7,
                                  encoding='utf-8')
    rf.suffix = "%Y-%m-%d_%H-%M.log"
    rf.setFormatter(formatter)
    rf.setLevel(level)
    logger1.addHandler(rf)
    sh = logging.StreamHandler(sys.stdout)
    sh.setLevel(level)
    sh.setFormatter(formatter)
    logger1.addHandler(sh)
    return logger1


logger = getLogger('./logs/equipment_alarm_min_max.log')
# 定义报警规则读取时间间隔（秒）
ALARM_INTERVAL = 10

# 定义数据查询向前偏移时间（秒）
SJ_XQPY = 8 * 60 * 60 + ALARM_INTERVAL
# 定义获取规则数据接口url
HQ_SJGZ = 'http://localhost:8087/digitized/rule/python/param'
# 定义获取规则数据接口参数
PAYLOAD = {'scriptTag': 'BCK'}
# 定义消费者线程数，报警信息保存线程数，大小值报警测点共 132 个
CUSTOMS_THREAD = 200
CUSTOMS_ALARM_THREAD = 10


def createGPConnect():
    """ 创建 GP 数据库连接,返回 gp 数据库连接 """
    count = 0
    while True:
        try:
            gp_con = psycopg2.connect(dbname="testdb", user="gpadmin", password="gpadmin", host="192.1.1.100", port="5432")
            cur = gp_con.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
            return gp_con, cur
        except Exception as e:
            logger.exception(e)
            time.sleep(10 * count)
            count += 1
            if count > 100:
                break


def createTSDBConnect():
    """ 创建 TSDB 数据库连接,返回tsdb 数据库 连接 """
    count = 0
    while True:
        try:
            tsdb_con = InfluxDBClient('192.1.1.100', 8086, 'admin', '123456', 'testdb')
            return tsdb_con
        except Exception as e:
            logger.exception(e)
            time.sleep(10 * count)
            count += 1
            if count > 100:
                break


def createRedisConnect():
    """ 创建 Redis 数据库连接,返回redis 数据库 连接池"""
    count = 0
    redis_conn = None
    while True:
        try:
            if redis_conn is None:
                pool = redis.ConnectionPool(host="192.1.1.100", port=6379, password="", max_connections=20)
                redis_conn = redis.Redis(connection_pool=pool)
            return redis_conn
        except Exception as e:
            logger.exception(e)
            time.sleep(10 * count)
            count += 1
            if count > 100:
                break


def before_now_time(second: int, utc: bool):
    # 获取当前时间偏差N秒
    nowTime = datetime.datetime.strptime(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "%Y-%m-%d %H:%M:%S")
    beforeTime = nowTime + datetime.timedelta(seconds=second)
    if utc:
        b = str(beforeTime).split(" ")
        beforeTime = b[0] + "T" + b[1] + "Z"
        n = str(nowTime).split(" ")
        nowTime = n[0] + "T" + n[1] + "Z"
    return [beforeTime, nowTime]


def utcTime_To_StandardTime(utc_str: str, utc_format: str, hours_i: int):
    """
    UTC时间字符串转换为时间戳 ("2019-11-11T12:15:05.786Z","%Y-%m-%dT%H:%M:%S.%fZ",8) return:2019-11-11 20:15:05.786000
    ("2019-11-11 12:15:05.786","%Y-%m-%dT%H:%M:%S.%fZ",0) return: 2019-11-11 12:15:05.786000
    """
    try:
        utcTime = datetime.datetime.strptime(utc_str, utc_format)  # "%Y-%m-%dT%H:%M:%S.%fZ"   "%Y-%m-%d %H:%M:%S.%f"
        standard = utcTime + datetime.timedelta(hours=hours_i)
        return standard
    except Exception as e:
        logger.exception(e)
        return utc_str


def format_To_UTCTime(standardstr: str, standard_format: str, target_format: str, hours_i: int = 0, second_i: int = 0):
    """
    UTC时间字符串转换为时间戳 ("2019-11-11 12:15:05.786","%Y-%m-%d %H:%M:%S.%f","%Y-%m-%dT%H:%M:%S.%fZ",hours_i=8)
        return:2019-11-11T20:15:05.786000Z
    ("2019-11-11 12:15:05.786","%Y-%m-%d %H:%M:%S.%f","%Y/%m/%d %H:%M:%S",hours_i=-1,second_i=30) return: 2019/11/11 11:15:35
    # "%Y-%m-%dT%H:%M:%S.%fZ"   "%Y-%m-%d %H:%M:%S.%f"
    """
    try:
        standTime = datetime.datetime.strptime(standardstr, standard_format)
        standardStr = standTime + datetime.timedelta(hours=hours_i, seconds=second_i)
        utcTime = datetime.datetime.strftime(standardStr, target_format)
        return utcTime
    except Exception as e:
        logger.exception(e)
        return standardstr


def producer(ruleQueue, thread):
    # 生产者，生产规则任务
    count = 0
    ruleData = None
    while True:
        try:
            if count > ALARM_INTERVAL * 10 or ruleData is None:
                req = requests.get(HQ_SJGZ, params=PAYLOAD)
                req.encoding = 'utf-8'
                html = json.loads(req.text)
                ruleData = html["data"]
                logger.info("获取最新规则- rule number:" + str(len(ruleData)) + " rule content:" + str(ruleData))
                ruleQueue.queue.clear()
                count = 0
            for m in ruleData:
                for i in m:
                    i['cal_time'] = before_now_time(ALARM_INTERVAL, False)
                    i['fail_try'] = 3
                    ruleQueue.put(i)
            count += ALARM_INTERVAL
            time.sleep(ALARM_INTERVAL)
        except Exception as e:
            logger.error("生产者获取规则异常----------------")
            logger.exception(e)
            time.sleep(ALARM_INTERVAL)


def consumers(ruleQueue, alarmQueue, thread):
    # tsdbCon = None
    redisConn = None
    while True:
        try:
            # if tsdbCon is None:
            #     tsdbCon = createTSDBConnect()
            if redisConn is None:
                redisConn = createRedisConnect()
            ruleContext = ruleQueue.get()
            # result = None
            # table_type = ruleContext["table_type"]
            # if table_type == "tsdb":
            #     time_split = ruleContext['cal_time']
            #       start_time = format_To_UTCTime(str(time_split[0]), "%Y-%m-%d %H:%M:%S", "%Y-%m-%dT%H:%M:%S.%fZ")
            #       end_time = format_To_UTCTime(str(time_split[1]), "%Y-%m-%d %H:%M:%S", "%Y-%m-%dT%H:%M:%S.%fZ")
            #       sql = "select " + ruleContext["en_name"] + " from " + ruleContext["table_en_name"] + " where " + \
            #             ruleContext[
            #                 "table_en_time"] + ">='" + start_time + "' and " + ruleContext[
            #               "table_en_time"] + "<='" + end_time + "' order by " + ruleContext["table_en_time"] + " DESC"
            #     sql = "select " + ruleContext["en_name"] + " from " + ruleContext["table_en_name"] + " order by " + \
            #           ruleContext["table_en_time"] + " DESC limit 1"
            #     result = tsdbCon.query(sql)
            #     logger.debug("query sql:{}".format(sql))
            # logger.debug("query result: {}".format(result))
            min_value = ''
            max_value = ''
            param_info = ruleContext["param_info"]
            for p in param_info:
                if p["code"] == "min":
                    min_value = p["value"]
                if p["code"] == "max":
                    max_value = p["value"]
            point_value_list = []
            # if table_type == "tsdb":
            #     for r in result.get_points():
            #         point_value_list.append([float(r[ruleContext["en_name"]]), r[ruleContext["table_en_time"]]])
            point_value = redisConn.hget(ruleContext["en_name"], 'value')
            point_timeStamp = redisConn.hget(ruleContext["en_name"], 'timeStamp')
            point_alarmFlag = redisConn.hget(ruleContext["en_name"], 'alarm_flag')
            rt = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(float(point_timeStamp) / 1000))
            logger.debug(thread + "--正在处理：{}".format(ruleContext["rule_name"] + "--》" + ruleContext["en_name"] +
                                                     ' 测点值：' + str(point_value) + ' 时间：' + rt +
                                                     ' 报警标识：' + str(point_alarmFlag)))
            if point_value is not None and point_timeStamp is not None:
                # real_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(float(point_timeStamp) / 1000))
                point_value_list.append([float(point_value), rt, float(point_timeStamp)])
            for pv in point_value_list:
                alarmFlag = 0
                ruleContext['point_value'] = pv
                if min_value != '' and pv[0] <= float(min_value):
                    alert_context = '小于最小值，报警值:' + str(pv[0]) + ';报警时间:' + str(pv[1])
                    ruleContext['alert_type'] = 2
                    ruleContext['alert_context'] = alert_context
                    alarmFlag = 2
                elif max_value != '' and pv[0] >= float(max_value):
                    alert_context = '大于最大值，报警值:' + str(pv[0]) + ';报警时间:' + str(pv[1])
                    ruleContext['alert_type'] = 2
                    ruleContext['alert_context'] = alert_context
                    alarmFlag = 2
                if point_alarmFlag is None or int(point_alarmFlag) != alarmFlag:
                    redisConn.hset(ruleContext["en_name"], 'alarm_flag', str(alarmFlag))
                    ruleContext['point_alarm_flag'] = alarmFlag
                    ruleContext['point_alarm_time'] = float(point_timeStamp)
                    alarmFlag = -1
                if alarmFlag != 0:
                    alarmQueue.put(ruleContext)

        except Exception as e:
            logger.error('消费者线程' + thread + " 处理失败：")
            logger.exception(e)
            ruleContext['fail_try'] -= 1
            if ruleContext['fail_try'] > 0:
                ruleQueue.put(ruleContext)


def consumersAlarm(alarmQueue, thread):
    gp_con, cur, device_info = None, None, {}
    while True:
        try:
            if gp_con is None or cur is None or len(device_info) <= 0:
                gp_con, cur = createGPConnect()
                cur.execute("select adp.point_en_name,bdad.device_name,bdad.device_id from bd.bd_app_device_point "
                            "AS adp LEFT JOIN bd.bd_app_device AS bdad ON adp.device_id=bdad.device_id")
                result = cur.fetchall()
                for i in range(len(result)):
                    device_info[result[i]['point_en_name']] = result[i]
            alarmContent = alarmQueue.get()
            # cur.execute(
            #     "select device_name,device_id from bd.bd_app_device where device_id in(select device_id from
            #     bd.bd_app_device_point where point_en_name=%s limit 1)" % (
            #             "'" + alarmContent["en_name"] + "'"))
            # deviceInfo = cur.fetchone()
            # device_name = deviceInfo["device_name"]
            # device_code = deviceInfo["device_id"]
            device_name = device_info[alarmContent["en_name"]]["device_name"]
            device_code = device_info[alarmContent["en_name"]]["device_id"]
            point_value = alarmContent['point_value']
            if 'alert_type' in alarmContent and 'alert_context' in alarmContent:
                alert_type = alarmContent['alert_type']
                alert_context = alarmContent['alert_context']
                # alarmTime = utcTime_To_StandardTime(point_value[1], "%Y-%m-%dT%H:%M:%S.%fZ", 8)
                alarmTime = point_value[2]
                ret = cur.execute(
                    "INSERT INTO bd.bd_uu_alert_num (device_name, device_code, create_time, alert_context,"
                    " production_line, call_type,  point_name, point_code, point_value, alert_param,alert_type)"
                    " VALUES (%s, %s,%s, %s,%s, %s,%s, %s,%s,%s,%s);"
                    % ("'" + device_name + "'", "'" + device_code + "'", str(alarmTime),
                       "'" + str(alert_context) + "'",
                       "'" + "万能二线轧线" + "'", "'" + str(1) + "'", "'" + alarmContent["ch_name"] + "'",
                       "'" + alarmContent["en_name"] + "'", "'" + str(point_value[0]) + "'",
                       "'" + json.dumps(alarmContent["param_info"]) + "'", "'" + str(alert_type) + "'"))
                logger.info("报警信息：{}".format(device_name + "," + device_code + "," + str(alarmTime) + "," +
                                             alert_context + "，" + "万能二线轧线" + "，" + str(alert_type) + "，" +
                                             alarmContent["ch_name"] + "," + alarmContent["en_name"] + "," +
                                             str(point_value[0]) + "," + json.dumps(alarmContent["param_info"])))
                alarmContent.pop('alert_type')
                alarmContent.pop('alert_context')
            if 'point_alarm_flag' in alarmContent and 'point_alarm_time' in alarmContent:
                alarm_flag = alarmContent['point_alarm_flag']
                alert_time = alarmContent['point_alarm_time']
                pv = point_value[0]
                logger.info("INSERT into bd.bd_uu_alert_status (device_name,device_code,point_name,point_code,"
                            "point_value,alert_tag,change_time)VALUES(%s,%s,%s,%s,%s,%s,%s);" % (
                                "'" + device_name + "'", "'" + device_code + "'", "'" + alarmContent["ch_name"] + "'",
                                "'" + alarmContent["en_name"] + "'", "'" + str(pv) + "'",
                                str(alarm_flag), str(alert_time)))
                cur.execute("INSERT into bd.bd_uu_alert_status (device_name,device_code,point_name,point_code,"
                            "point_value,alert_tag,change_time)VALUES(%s,%s,%s,%s,%s,%s,%s);" % (
                                "'" + device_name + "'", "'" + device_code + "'", "'" + alarmContent["ch_name"] + "'",
                                "'" + alarmContent["en_name"] + "'", "'" + str(pv) + "'",
                                str(alarm_flag), str(alert_time)))
                alarmContent.pop('point_alarm_flag')
                alarmContent.pop('point_alarm_time')
            gp_con.commit()
        except Exception as e:
            logger.error("生产者获取规则异常----------------" + thread)
            logger.exception(e)
            gp_con.commit()


def main():
    # 创建队列
    ruleQueue = Queue(CUSTOMS_THREAD * 2)
    alarmQueue = Queue(CUSTOMS_THREAD)
    thread_pro = threading.Thread(target=producer, args=(ruleQueue, '规则分配线程'))
    pthread_list = [thread_pro]
    for i in range(CUSTOMS_THREAD):
        thread_cus = threading.Thread(target=consumers, args=(ruleQueue, alarmQueue, "监控消费线程{}".format(i + 1)))
        pthread_list.append(thread_cus)
    for i in range(CUSTOMS_ALARM_THREAD):
        thread_cus = threading.Thread(target=consumersAlarm, args=(alarmQueue, "报警消费线程{}".format(i + 1)))
        pthread_list.append(thread_cus)

    for i in pthread_list:
        i.start()
    for i in pthread_list:
        i.join
    return 0


if __name__ == '__main__':
    main()
