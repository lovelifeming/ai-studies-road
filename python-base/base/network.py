#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/5/12 10:39
# @Author : zengsm
# @File : network
import datetime

import requests
from bs4 import BeautifulSoup


def add_github_host(sys: str = 'windows'):
    """ 一般Github的访问有两部分：主站的访问和二级域名的资源加载（比如样式文件等）一般Github加载缓慢，主要是
     assets-cdn.github.com、avatars0.githubusercontent.com 以及 avatars1.githubusercontent.com 三个域名的解析问题。
    为了提高速度，可以使用HOSTS加速对Github的域名解析。查看国内能解析的DNS： http://tool.chinaz.com/dns
    解决办法，修改hosts主机映射文件：
    windows C:\Windows\System32\drivers\etc\hosts
    linux /etc/hosts
    添加github一系列网址的IP地址、域名映射
    原理就是：当我们访问github时，那些域名什么的就不需要去DNS服务器上询问了，直接从本地HOST文件中获得。"""
    s = """
	github.io
    github.com
	raw.github.com
	help.github.com	
	status.github.com
	training.github.com
	nodeload.github.com
    assets-cdn.github.com
	github.githubassets.com
	documentcloud.github.com
    avatars0.githubusercontent.com
    avatars1.githubusercontent.com
    avatars2.githubusercontent.com"""
    ans = []
    for i in s.split():
        # http://ip.tool.chinaz.com/    http://ip.chinaz.com/
        url = "http://ip.tool.chinaz.com/" + i.strip()
        resp = requests.get(url)
        soup = BeautifulSoup(resp.text)
        x = soup.find(class_="IcpMain02")
        x = x.find_all("span", class_="Whwtdhalf")
        x = "%s %s" % (x[5].string.strip(), i.strip())
        print(x)
        ans.append(x)

    hosts = r"C:\Windows\System32\drivers\etc\hosts" if sys is 'windows' else '/etc/hosts'
    print('hosts file path:' + hosts)
    print(ans)
    with open(hosts, "a") as f:
        f.write('\n')
        f.write('### add new ip address and host name by time: ' + datetime.datetime.now().__str__() + '\n')
        f.writelines('\n'.join([i for i in ans]))


if __name__ == '__main__':
    # add_github_host()  # 添加 github 地址映射
    t = datetime.date.strftime(datetime.datetime(datetime.datetime.today().year, datetime.datetime.today().month, 1) - datetime.timedelta(1),"%Y-%m")
    print(t)
    print(type(t))
    print('end...')
