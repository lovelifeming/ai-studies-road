#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/9/3 16:01
# @File : test
import json
import time

import requests
import urllib3

from base.network import Ipv4_range

if __name__ == '__main__':
    print('start ...')
    # urllib3.disable_warnings()
    # cookies = 'JSESSIONID=-dsnP1KWKQnPnEy5ef3XV_QC6-fYVjbw5wCrD-U4; satoken=10d56dff952f4eed9933f4b06a18427e'
    # # token = '9a469a6783716bb075e4a1defe0337dd'
    # header = {'Accept': 'application/json, text/plain, */*',
    #           'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'zh-CN,zh;q=0.9',
    #           'Connection': 'keep-alive',
    #           'Content-Length': '131',
    #           'Content-Type': 'application/json;charset=UTF-8',
    #           'Cookie': cookies,
    #           'Host': '10.6.67.181',
    #           'Origin': 'https://10.6.67.181',
    #           'Referer': 'https://10.6.67.181/securityConf/ruleManage',
    #           'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
    #           'sec-ch-ua-mobile': '?0',
    #           'sec-ch-ua-platform': '"Windows"',
    #           'Sec-Fetch-Dest': 'empty',
    #           'Sec-Fetch-Mode': 'cors',
    #           'Sec-Fetch-Site': 'same-origin',
    #           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36',
    #           'X-Requested-With': 'XMLHttpRequest'}
    # ip_addr = '10.6.67.181'
    # gradeMap = {10: '无威胁', 20: '低', 30: '中', 40: '高'}
    # file = open('D:\\data.txt', 'w')
    # for i in range(1, 436):
    #     list_url = 'https://10.6.67.181/api/event/eventRulePage'
    #     datas = {'desc': 'true', 'enabled': '', 'eventType': [], 'name': '', 'pageNum': i, 'pageSize': 10,
    #              'protocol': [], 'ruleType': [], 'threatLevel': [], 'type': 0}
    #     response = requests.post(list_url, json=datas, headers=header, verify=False)
    #     print(response.text)
    #     print(response.request.headers)
    #     if not response.json()['success']:
    #         print("connect fail!")
    #         break
    #     list_data = response.json()['data']['records']
    #     for x in list_data:
    #         guid = x['id']
    #         gid = x['gid']
    #         detail_url = 'https://10.6.67.181/api/event/detail'
    #         datas1 = {'gid': gid, 'surId': guid}
    #         time.sleep(0.1)
    #         dt_response = requests.post(detail_url, headers=header, json=datas1, verify=False)
    #         dt = dt_response.json()['data']
    #         grade = gradeMap[x['threatLevel']]
    #         sql = "INSERT INTO `db_nssa`.`sys_risk1` (`user_id`, `enterprise_id`, `device`, `risk_type`," \
    #               " `risk_name`, `risk_des`, `risk_suggestion`, `risk_grade`, `remark`, `create_time`, `risk_class`) VALUES " \
    #               "(0, 0, '{}', '{}', '{}', '{}', '{}', '{}', NULL ,now(),'{}');".format(str(ip_addr),
    #                                                                                      '启明星辰探针', x['name'],
    #                                                                                      x['description'],
    #                                                                                      dt['suggestion'], grade,
    #                                                                                      x['attackFunc'])
    #
    #         file.write(sql + '\n')
    #
    # file.close()
    # https://blog.csdn.net/SheYanxiao/article/details/124648710
    res = """{
	"syslog_system_sec": {
		"aliases": {},
		"mappings": {
			"date_detection": false,
			"properties": {
				"asset_area_id": {
					"type": "text",
					"fields": {
						"keyword": {
							"type": "keyword",
							"ignore_above": 256
						}
					}
				},
				"asset_id": {
					"type": "text",
					"fields": {
						"keyword": {
							"type": "keyword",
							"ignore_above": 256
						}
					}
				},
				"asset_important": {
					"type": "text",
					"fields": {
						"keyword": {
							"type": "keyword",
							"ignore_above": 256
						}
					}
				},
				"asset_ip": {
					"type": "text",
					"fields": {
						"keyword": {
							"type": "keyword",
							"ignore_above": 256
						}
					}
				},
				"asset_ip_num": {
					"type": "text",
					"fields": {
						"keyword": {
							"type": "keyword",
							"ignore_above": 256
						}
					}
				},
				"asset_name": {
					"type": "text",
					"fields": {
						"keyword": {
							"type": "keyword",
							"ignore_above": 256
						}
					}
				},
				"asset_unit_id": {
					"type": "text",
					"fields": {
						"keyword": {
							"type": "keyword",
							"ignore_above": 256
						}
					}
				},
				"create_time": {
					"type": "text",
					"fields": {
						"keyword": {
							"type": "keyword",
							"ignore_above": 256
						}
					}
				},
				"dvcid": {
					"type": "text",
					"fields": {
						"keyword": {
							"type": "keyword",
							"ignore_above": 256
						}
					}
				},
				"dvcip": {
					"type": "text",
					"fields": {
						"keyword": {
							"type": "keyword",
							"ignore_above": 256
						}
					}
				},
				"enterprise_id": {
					"type": "text",
					"fields": {
						"keyword": {
							"type": "keyword",
							"ignore_above": 256
						}
					}
				},
				"facility": {
					"type": "text",
					"fields": {
						"keyword": {
							"type": "keyword",
							"ignore_above": 256
						}
					}
				},
				"facility_des": {
					"type": "text",
					"fields": {
						"keyword": {
							"type": "keyword",
							"ignore_above": 256
						}
					}
				},
				"happen_time": {
					"type": "date",
					"format": "yyyy-MM-dd HH:mm:ss"
				},
				"info": {
					"type": "text",
					"fields": {
						"keyword": {
							"type": "keyword",
							"ignore_above": 256
						}
					}
				},
				"priority": {
					"type": "text",
					"fields": {
						"keyword": {
							"type": "keyword",
							"ignore_above": 256
						}
					}
				},
				"risk_des": {
					"type": "text",
					"fields": {
						"keyword": {
							"type": "keyword",
							"ignore_above": 256
						}
					}
				},
				"risk_grade": {
					"type": "text",
					"fields": {
						"keyword": {
							"type": "keyword",
							"ignore_above": 256
						}
					}
				},
				"risk_type": {
					"type": "text",
					"fields": {
						"keyword": {
							"type": "keyword",
							"ignore_above": 256
						}
					}
				},
				"rowkey": {
					"type": "text",
					"fields": {
						"keyword": {
							"type": "keyword",
							"ignore_above": 256
						}
					}
				},
				"rowlog": {
					"type": "text",
					"fields": {
						"keyword": {
							"type": "keyword",
							"ignore_above": 256
						}
					}
				},
				"security": {
					"type": "text",
					"fields": {
						"keyword": {
							"type": "keyword",
							"ignore_above": 256
						}
					}
				},
				"security_des": {
					"type": "text",
					"fields": {
						"keyword": {
							"type": "keyword",
							"ignore_above": 256
						}
					}
				},
				"short_ts": {
					"type": "text",
					"fields": {
						"keyword": {
							"type": "keyword",
							"ignore_above": 256
						}
					}
				},
				"types": {
					"type": "text",
					"fields": {
						"keyword": {
							"type": "keyword",
							"ignore_above": 256
						}
					}
				}
			}
		},
		"settings": {
			"index": {
				"number_of_shards": "9",
				"translog": {
					"flush_threshold_size": "1gb",
					"sync_interval": "30s",
					"durability": "async"
				},
				"blocks": {
					"read_only_allow_delete": "false"
				},
				"provided_name": "syslog_system_sec",
				"creation_date": "1647336549705",
				"number_of_replicas": "1",
				"uuid": "XUvQqfJTSeiLSk8WN590jg",
				"version": {
					"created": "7040299"
				}
			}
		}
	}
}"""
    # jn = json.loads(res)
    # mp = jn['syslog_system_sec']['mappings']['properties']
    # print(len(mp))
    # res=''
    # for k,v in mp.items():
    #     tp='varchar(32)'
    #     if v['type'] == 'long':
    #         tp='BIGINT'
    #     elif v['type'] == 'date':
    #         tp='date'
    #     elif v['type'] == 'datetime':
    #         tp='datetime'
    #     res+='`'+k+'` '+tp+' NULL DEFAULT NULL COMMENT \'' + k +'\',\r\n'
    # print(res)
    ips = Ipv4_range()
    a= ips.ips('10.90.3.1/30')
    print(a)

    # ip_range = Ipv6_range()
    # ip = 'fe80:8000:480a::1741/127'
    # a = ip_range.ips(ip)
    # print(a)

    print('end ...')
