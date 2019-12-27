# encoding: utf-8
import datetime
import logging
import time

# 固定时间间隔采集数据
import psycopg2.extras
from influxdb import InfluxDBClient

# 创建一个logger
logger = logging.getLogger('mylogger')
logger.setLevel(logging.DEBUG)

# 创建一个handler，用于写入日志文件
fh = logging.FileHandler('equipment_fixed_rate.log', encoding='UTF-8')
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


def print_ts(message):
    print("[%s] %s" % (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), message))


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


def run():
    while True:
        try:
            while True:
                now = datetime.datetime.now()
                # 到达设定时间，结束内循环 now.hour in [0, 8, 16] and now.minute in [0,10,20,30,40,50] and now.second in [0]
                if now.minute in [0]:
                    break
                # 时间没到就等n秒之后再次检测
                time.sleep(60)
            gp_db, cur, client = create_con()
            sql = "select Pos_Load_Material_HF from BD_UU_NEW_HF1 order by time DESC limit 1"
            result = client.query(sql)
            print('tsdb查询结果：' + str(result))
            point_value_list = []
            for r in result.get_points():
                point_value_list.append([r["Pos_Load_Material_HF"], r["time"]])
            if len(point_value_list):
                utcTime = point_value_list[0][1]
                print("point_value_list:" + str(point_value_list))
                standTime = utcTime_To_StandardTime(utcTime, "%Y-%m-%dT%H:%M:%S.%fZ", 8)
                ret = cur.execute("INSERT INTO bd.deterioration_trend "
                                  "(acq_time,process_en_name,device_id,variable_code,value) VALUES (%s,%s,%s,%s,%s)"
                                  % ("'" + str(standTime) + "'", "'" + "HF" + "'", "'" + "114001001" + "'",
                                     "'" + "Pos_Load_Material_HF" + "'", "'" + str(point_value_list[0][0]) + "'"))
                gp_db.commit()
                time.sleep(60)
        except Exception as e:
            logger.exception(e)


def utcTime_To_StandardTime(utc_str: str, utc_format: str, hours_i: int):
    """
    UTC时间字符串转换为时间戳 ("2019-09-20T09:12:04.979Z","%Y-%m-%dT%H:%M:%S.%fZ",8) return:2019-09-20 17:12:04.970000
    """
    try:
        utcTime = datetime.datetime.strptime(utc_str, utc_format)  # "%Y-%m-%dT%H:%M:%S.%fZ"   "%Y-%m-%d %H:%M:%S.%f"
        standard = utcTime + datetime.timedelta(hours=hours_i)
        return standard
    except Exception as e:
        logger.exception(e)
        return utc_str


if __name__ == '__main__':
    run()
