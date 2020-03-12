# encoding: utf-8
import datetime
import json
import logging
import threading
import time
from queue import Queue

import psycopg2.extras
import requests
from influxdb import InfluxDBClient

# 定义报警规则处理时间间隔（秒）
GZ_READ_TIME = 20
# 定义数据查询向前偏移时间（秒）
SJ_XQPY = 8 * 60 * 60 + GZ_READ_TIME
# 定义获取规则数据接口lurl
HQ_SJGZ = 'http://localhost:8087/digitized/rule/python/param'
# 定义获取规则数据接口参数
PAYLOAD = {'scriptTag': 'FIXED_ALARM_TRUE'}
# 定义消费者线程数
CUSTOM_THREAD = 20


# 创建数据库连接
def create_con():
    gp_db, cur, client = None, None, None
    while True:
        try:
            if gp_db is None or cur is None or client is None:
                gp_con = psycopg2.connect(dbname="testdb", user="gpadmin", password="gpadmin", host="192.1.1.100",
                                          port="5432")
                cur = gp_db.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
                client = InfluxDBClient('192.1.1.100', 8086, 'admin', '123456', 'testdb')
            return gp_db, cur, client
        except Exception as e:
            logger.error("数据库连接异常----------------------")
            logger.exception(e)


# 获取当前时间前n秒
def now_time():
    now_time = datetime.datetime.now()
    now_old = now_time + datetime.timedelta(seconds=-SJ_XQPY)
    now_old = str(now_old)
    now_old_split = now_old.split(" ")
    now_old = now_old_split[0] + "T" + now_old_split[1] + "Z"
    now_time = str(now_time)
    now_time_split = now_time.split(" ")
    now_time = now_time_split[0] + "T" + now_time_split[1] + "Z"
    return [now_old, now_time]


def str_to_timestamp(utc_str: str, utc_format: str, hours_i: int):
    """
    UTC时间字符串转换为时间戳
    """
    timeArray = time.strptime(utc_str, utc_format)
    timeStamp = (int(time.mktime(timeArray)) + hours_i * 60 * 60) * 1000
    return timeStamp


# 创建一个logger
logger = logging.getLogger('mylogger')
logger.setLevel(logging.DEBUG)

# 创建一个handler，用于写入日志文件
fh = logging.FileHandler('equipment_alarm_fixed_alarm_true.log', encoding='UTF-8')
fh.setLevel(logging.DEBUG)

# 再创建一个handler，用于输出到控制台
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# 定义handler的输出格式
formatter = logging.Formatter('[%(asctime)s][%(thread)d][%(filename)s][line: %(lineno)d][%(levelname)s] ## %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)

# 给logger添加handler
logger.addHandler(fh)
logger.addHandler(ch)

# 创建队列
fifo = Queue(200)
# 创建待处理列表
wait = []
# 创建处理失败列表
fail = []


# 生成任务队列
def producers():
    count = 0
    mll = None
    while True:
        try:
            if count > GZ_READ_TIME * 100 or mll is None:
                resp = requests.get(HQ_SJGZ, params=PAYLOAD)
                resp.encoding = 'utf-8'
                #   json解析
                html = json.loads(resp.text)
                mll = html["data"]
                logger.info("producers->where 规则获取- rule number:" + str(len(mll)) + " rule content:" + str(mll))
                # 将最新规则，加入任务队列
                fifo.queue.clear()
                count = 0
            for m in mll:
                for i in m:
                    i['cal_time'] = now_time()
                    i['fail_count'] = 3
                    fifo.put(i)
            count += GZ_READ_TIME
            time.sleep(GZ_READ_TIME)
        except Exception as e:
            logger.error("生产者获取规则异常——————————")
            logger.exception(e)
            if e == "## cursor already closed":
                create_con()


# 消费者线程--处理数据
def consumers(q_fifo, thread):
    gp_db, cur, client = None, None, None
    con_flag = False
    while True:
        try:
            if cur is None or con_flag:
                gp_db_c, cur_c, client_c = create_con()
                gp_db, cur, client = gp_db_c, cur_c, client_c
            clx = q_fifo.get()
            logger.info(thread + "--正在处理：{},队列剩余：{}".format(clx["rule_name"] + "--》" + clx["en_name"], fifo.qsize()))
            logger.info(str(clx))
            call_type = 0
            alert_context = ""

            # 获得库源
            result = None
            table_type = clx["table_type"]
            # if table_type == "gp":
            #     time_split = now_time()
            #     start_time = time_split[0].replace("T", " ").replace("Z", "")
            #     end_time = time_split[1].replace("T", " ").replace("Z", "")
            #     sql = "select " + clx["en_name"] + "," + clx["table_en_time"] + " from " + clx[
            #         "table_en_name"] + " where " + clx["table_en_time"] + ">='" + start_time + "' and " + clx[
            #               "table_en_time"] + "<='" + end_time + "' order by " + clx["table_en_time"] + " desc"
            #     logger.info("execute sql:" + sql)
            #     cur.execute(sql)
            #     result = cur.fetchall()
            if table_type == "tsdb":
                time_split = clx['cal_time']
                start_time = time_split[0]
                end_time = time_split[1]
                # sql = "select " + clx["en_name"] + " from " + clx["table_en_name"] + " where " + clx[
                #     "table_en_time"] + ">='" + start_time + "' and " + clx[
                #           "table_en_time"] + "<='" + end_time + "' order by " + clx["table_en_time"] + " desc"
                sql = "select " + clx["en_name"] + " from " + clx["table_en_name"] + " order by " + clx["table_en_time"] + " DESC limit 1"
                # logger.info(thread + "execute sql:" + sql)
                result = client.query(sql)
            logger.info(thread + " query result: " + str(table_type) + str(result))
            # 写自己的报警逻辑，决定call_type的值，true位报警，false为不报警
            alarm_value = ''
            param_info = clx["param_info"]
            for p in param_info:
                if p["code"] == "alarm_value":
                    alarm_value = p["value"]
            point_value_list = []
            point_value = None
            point_value_time = ''
            # if table_type == "gp":
            #     for r in result:
            #         point_value_list.append([float(r[clx["en_name"].lower()]), r[clx["table_en_time"]]])
            if table_type == "tsdb":
                for r in result.get_points():
                    point_value_list.append([float(r[clx["en_name"]]), r[clx["table_en_time"]]])
            if alarm_value != '':
                for pv in point_value_list:
                    if pv[0] == alarm_value:
                        point_value = pv[0]
                        point_value_time = pv[1]
                        alert_context = "报警值:" + str(pv[0])
                        call_type = 1
            if call_type == 1:
                # 处理成功从待处理列表中移除 查询设备名
                cur.execute("select device_name,device_id from bd.bd_app_device where device_id in"
                            "(select device_id from bd.bd_app_device_point where point_en_name=%s limit 1)" % (
                                    "'" + clx["en_name"] + "'"))
                sb = cur.fetchone()
                device_name = sb["device_name"]
                device_code = sb["device_id"]
                # 获取报警时间
                timestamp = None
                # if table_type == "gp":
                #     timestamp = str_to_timestamp(str(point_value_time), "%Y-%m-%d %H:%M:%S.%f", 0)
                if table_type == "tsdb":
                    timestamp = str_to_timestamp(point_value_time, "%Y-%m-%dT%H:%M:%S.%fZ", 8)
                ret = cur.execute(
                    "INSERT INTO bd.bd_uu_alert_num (device_name, device_code, create_time, alert_context,"
                    "production_line, call_type,  point_name, point_code, point_value, alert_param)"
                    " VALUES (%s, %s,%s, %s,%s, %s,%s, %s,%s,%s);"
                    % ("'" + device_name + "'", "'" + device_code + "'", timestamp, "'" + alert_context + "'",
                       "'" + "万能二线轧线" + "'", "'" + str(call_type) + "'", "'" + clx["ch_name"] + "'",
                       "'" + clx["en_name"] + "'", "'" + str(point_value) + "'",
                       "'" + str(clx["param_info"]) + "'"))
                gp_db.commit()
                logger.info("报警详细信息：" + device_name + "," + device_code + "," + timestamp + "," +
                            alert_context + "," + "万能二线轧线" + "," + str(call_type) + "," + clx["ch_name"] + "," +
                            clx["en_name"] + "," + str(point_value) + "," + str(clx["param_info"]))
        # 程序异常，继续处理
        except Exception as e:
            logger.error("生产者处理报警异常——————————")
            if str(e) in "## gp cursor already closed" or str(e) in "## server closed the connection unexpectedly":
                con_flag = False
            if 'clx' in dir() and clx['fail_count'] >= 0:
                clx['fail_count'] -= 1
                fifo.put(clx)
                logger.error('异常处理报警规则：' + str(clx))
            logger.exception(e)
        # time.sleep(GZ_HANDLE_TIME)


def main():
    # 建立1个生产者线程
    thread_pro = threading.Thread(target=producers)
    pthread_list = [thread_pro]
    # 建立10个消费者线程
    for i in range(CUSTOM_THREAD):
        thread_cus = threading.Thread(target=consumers, args=(fifo, "消费线程{}".format(i + 1)))
        pthread_list.append(thread_cus)
    for i in pthread_list:
        i.start()
    for i in pthread_list:
        i.join
    return 0


if __name__ == '__main__':
    main()
