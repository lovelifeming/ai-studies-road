# reload(sys)
# sys.setdefaultencoding( "utf-8" )



# if __name__=='__main__':
#     start()



# from pyspark import SparkContext,SparkConf
# from pyspark.streaming import StreamingContext
# from pyspark.streaming.kafka import KafkaUtils
# from thrift import Thrift
# from thrift.transport import TSocket
# from thrift.transport import TTransport
# from thrift.protocol import TBinaryProtocol
# from hbase import Hbase
# from hbase.ttypes import *
# import re
# import json
# import time
# import MySQLdb
#
# reload(sys)
# sys.setdefaultencoding( "utf-8" )
#
# conn = MySQLdb.connect(host='hadoop3',user='root',passwd='bigdata',db='table_code',charset='utf8')
# cur = conn.cursor()
# sql = "SELECT * FROM table_code"
# cur.execute(sql)
# code_data = cur.fetchall()
# table_dict = {}
# for row in code_data:
# 	databasename = row[0]
# 	tablename = row[1]
# 	tablecode = row[2]
# 	if databasename not in table_dict:
# 		table_dict[databasename] = {}
# 	table_dict[databasename][tablename] = tablecode
# cur.close()
# conn.close()
# transport = TSocket.TSocket('hadoop2', 9090)
# protocol = TBinaryProtocol.TBinaryProtocol(transport)
# client = Hbase.Client(protocol)
# def start():
# 	sc = SparkContext(appName="pyspark kafka-spark-streaming-hbase")
# 	ssc = StreamingContext(sc, 1)
# 	brokers = "hadoop2:9092,hadoop3:9092,hadoop4:9092,hadoop5:9092,hadoop6:9092"
# 	topics = ['test_db']
# 	zkQuorum = 'hadoop2:2181,hadoop3:2181,hadoop4:2181,hadoop5:2181,hadoop6:2181'
# 	kvs = KafkaUtils.createDirectStream(ssc, topics, {"metadata.broker.list": brokers})
# 	lines = kvs.map(lambda x: x[1])
# 	lines.foreachRDD(lambda rdd : rdd.foreach(lambda msg : execute(msg)))
# 	ssc.start()
# 	ssc.awaitTermination()
#
# def execute(msg):
# 	transport.open()
# 	try:
# 		msg = msg.encode('unicode-escape').decode('string_escape')
# 		json_data = json.loads(msg)
# 		exe_type = json_data['type']
# 		database = json_data['database']
# 		tablename = json_data['tablename']
# 		tablecode = table_dict[database][tablename]
# 		row = json_data['row']
# 		hbase_tablename = '%s_%s' %('BIGDATA',database.upper())
# 		hbase_tablename = hbase_tablename.encode('unicode-escape').decode('string_escape')
# 		rowkey = '%s_%s' %(tablecode,row)
# 		rowkey = rowkey.encode('unicode-escape').decode('string_escape')
# 		mutations = []
# 		if exe_type == 'delete':
# 			mutations.append(Mutation(column='cf:delfsnip',value='1'))
# 		else:
# 			data = json_data['data']
# 			for field,thevalue in data.items():
# 				field = field.encode('unicode-escape').decode('string_escape')
# 				thevalue = thevalue.encode('unicode-escape').decode('string_escape')
# 				mutations.append(Mutation(column='cf:%s' %(field),value=thevalue))
# 			if exe_type == 'insert':
# 				mutations.append(Mutation(column='cf:delfsnip',value='0'))
# 		client.mutateRow(hbase_tablename,rowkey,mutations)
# 		thetime = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
# 	except:
# 		transport.close()
# 		return
# 	transport.close()
# if __name__ == '__main__':
# 	start()

# reload(sys)
# sys.setdefaultencoding( "utf-8" )
#coding: utf-8
# import sys
# from imp import reload
#
# reload(sys)
# sys.setdefaultencoding('utf8')
#
field="中华人公告"

# def start():
#     field = "中华人公告"
#     field = field.encode('unicode-escape').decode('string_escape')
#     print(field)
#
# if __name__=='__main__':
#     start()
# !/usr/bin/python3
a=field.encode('unicode-escape')
print(a)
b=a.decode('string_escape')






# print(b)
#  print(field.encode('unicode-escape').decode('string_escape'))



