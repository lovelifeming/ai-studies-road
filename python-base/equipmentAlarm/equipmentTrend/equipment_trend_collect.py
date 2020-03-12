# encoding: utf-8
import datetime
import logging
import time

import psycopg2.extras
from influxdb import InfluxDBClient

# 定义报警规则读取时间间隔（秒）
GZ_READ_TIME = 60 * 60
# 定义报警规则处理时间间隔（秒）
GZ_HANDLE_TIME = 10 * 60
# 定义数据查询向前偏移时间（秒）
SJ_XQPY = 8 * 60 * 60 + 20 * 60
# 标准时间与东八区Beijing时间差（秒）
UTC_STANDARD = 8 * 60 * 60
# 定义获取规则数据接口url
HQ_SJGZ = 'http://localhost:8087/digitized/rule/python/param'
# 定义获取规则数据接口参数
PAYLOAD = {'scriptTag': 'FIXED_RATE'}
# 定义消费者线程数
CUS = 2
# 处理测点参数，测点，表名          114001001 114001002
POINT_TUPLE = (
    ['Nor_Pos_S_Ste_Fur_Bea_HF1', 'Nor_Pos_Lif_Ste_Fur_Bea_HF1', 'Pos_Fuel_Tank_HF1', 'BD_UU_NEW_HF1', '114001001'],
    ['Nor_Pos_S_Ste_Fur_Bea_HF2', 'Nor_Pos_Lif_Ste_Fur_Bea_HF2', 'Pos_Fuel_Tank_HF2', 'BD_UU_NEW_HF2', '114001002'])

# 一号液压站114001001：
# Nor_Pos_S_Ste_Fur_Bea_HF1,Nor_Pos_Lif_Ste_Fur_Bea_HF1,Pos_Fuel_Tank_HF1   上料液压站油箱液位: Pos_Load_Material_HF
# 二号液压站114001002：
# Nor_Pos_S_Ste_Fur_Bea_HF2,Nor_Pos_Lif_Ste_Fur_Bea_HF2,Pos_Fuel_Tank_HF2

# 创建数据库连接
def create_con():
    while True:
        try:
            gp_db = psycopg2.connect(dbname="testdb", user="gpadmin", password="gpadmin", host="192.1.1.100", port="5432")
            cur = gp_db.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
            # 连接tsdb数据库
            client = InfluxDBClient('192.1.1.100', 8086, 'admin', '123456', 'testdb')
            return gp_db, cur, client
        except Exception as e:
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


def utcTime_To_StandardTime(utc_str: str, utc_format: str, hours_i: int):
    """
    UTC时间字符串转换为时间戳 ("2019-09-20T09:12:04.979Z","%Y-%m-%dT%H:%M:%S.%fZ",8) return:2019-09-20 17:12:04.979000
    """
    try:
        utcTime = datetime.datetime.strptime(utc_str, utc_format)  # "%Y-%m-%dT%H:%M:%S.%fZ"   "%Y-%m-%d %H:%M:%S.%f"
        standard = utcTime + datetime.timedelta(hours=hours_i)
        return standard
    except Exception as e:
        logger.exception(e)
        return utc_str


def str_to_timestamp(utc_str: str, utc_format: str):
    """
    UTC时间字符串转换为时间戳
    """
    timeArray = time.strptime(utc_str, utc_format)
    timeStamp = int(time.mktime(timeArray) + UTC_STANDARD) * 1000
    return timeStamp


# 创建一个logger
logger = logging.getLogger('mylogger')
logger.setLevel(logging.DEBUG)
# 创建一个handler，用于写入日志文件
fh = logging.FileHandler('equipment_trend_collect.log', encoding='UTF-8')
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


def consumers(params):
    while True:
        try:
            run(params[0])
            run(params[1])
        # 程序异常，继续处理
        except Exception as e:
            logger.exception("equipment trend collect：液压站趋势统计异常", e)
        time.sleep(GZ_HANDLE_TIME)


def run(params):
    gp_db_c, cur_c, client_c = create_con()
    gp_db, cur, client = gp_db_c, cur_c, client_c
    time_split = now_time()
    start_time = time_split[0]
    end_time = time_split[1]

    sql = "select " + params[0] + " from " + params[3] + " where time" + ">='" + start_time \
          + "' and time" + "<='" + end_time + "' order by time DESC"
    result = client.query(sql)
    point_value_list = []
    logger.info(params)
    logger.info("查询结果："+ str(result))
    for r in result.get_points():
        t = r['time']
        standTime = utcTime_To_StandardTime(t, "%Y-%m-%dT%H:%M:%S.%fZ", 8)
        seconds = (datetime.datetime.now() - standTime).total_seconds()
        v = r[params[0]]
        if v is False and seconds < 60 * 10:
            return
        elif v is True and seconds > 60 * 10:
            point_value_list.append([v, t])
            break
    if len(point_value_list) == 0 and len(result) != 0:
        return

    sql1 = "select " + params[1] + " from " + params[3] + " where time" + ">='" + start_time \
           + "' and time" + "<='" + end_time + "' order by time DESC"
    result1 = client.query(sql1)
    logger.info("查询结果："+ str(result))
    point_value_list1 = []
    for r in result1.get_points():
        t = r['time']
        standTime1 = utcTime_To_StandardTime(t, "%Y-%m-%dT%H:%M:%S.%fZ", 8)
        seconds1 = (datetime.datetime.now() - standTime1).total_seconds()
        v = r[params[1]]
        if v is False and seconds1 < 60 * 10:
            return
        if seconds1 > 60 * 10 and v is True:
            point_value_list1.append([v, t])
            break
    if len(point_value_list1) == 0 and len(result) != 0:
        return

    sql = "select " + params[2] + " from " + params[3] + " order by time DESC limit 1"
    result = client.query(sql)
    point_value_list2 = []
    print('tsdb查询结果：' + str(result))
    for r in result.get_points():
        point_value_list2.append([r["time"], r[params[2]]])
    logger.info("液压站归位液位：" + str(point_value_list2))
    if len(point_value_list2):
        utcTime2 = point_value_list2[0][0]
        print("point_value_list:" + str(point_value_list2))
        standTime2 = utcTime_To_StandardTime(utcTime2, "%Y-%m-%dT%H:%M:%S.%fZ", 8)
        insertSQL = str(u"INSERT INTO bd.deterioration_trend "
                        "(acq_time,process_en_name,device_id,variable_code,value) VALUES (%s,%s,%s,%s,%s)"
                        % ("'" + str(standTime2) + "'", "'" + "HF" + "'", "'" + params[4] + "'",
                           "'" + params[2] + "'", "'" + str(point_value_list2[0][1]) + "'"))
        logger.info(" insert sql:" + insertSQL)
        ret = cur.execute(insertSQL)
        gp_db.commit()


def main():
    logger.info("equipment trend collect：液压站趋势统计开始.")
    consumers(POINT_TUPLE)
    logger.info("equipment trend collect：液压站趋势统计结束.")


if __name__ == '__main__':
    main()
