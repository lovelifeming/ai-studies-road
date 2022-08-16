#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/5/12 10:39
# @Author : zengsm
# @File : network
import datetime

import requests
from bs4 import BeautifulSoup


class Ipv4_range:
    """ IPv4的地址和掩码转换为地址范围 """

    def part(self, part_ip, part_mask):
        part_ip = int(part_ip)
        part_mask = int(part_mask)
        delta = 255 - part_mask

        ip_min = part_ip & part_mask
        ip_max = ip_min + delta
        return ip_min, ip_max

    def ips(self, ip_mask):
        sep = ip_mask.split('/')
        ip = sep[0]
        mask = self.msk_trans(sep[1])
        return self.ip(ip, mask)

    def ip(self, ip, mask):
        part_ips = ip.split('.')
        part_masks = mask.split('.')
        ip_min = ''
        ip_max = ''
        for i in range(0, 4):
            part_min, part_max = self.part(part_ips[i], part_masks[i])
            ip_min += str(part_min) + '.'
            ip_max += str(part_max) + '.'
        ip_min = ip_min[:-1]
        ip_max = ip_max[:-1]
        return ([ip_min, ip_max])

    def msk_trans(self, digit):
        add = 32 - int(digit)
        msk_str_b = '1' * int(digit) + '0' * add

        msk1 = msk_str_b[0:8]
        msk2 = msk_str_b[8:16]
        msk3 = msk_str_b[16:24]
        msk4 = msk_str_b[24:32]

        msk1_deci = int(msk1, 2)
        msk2_deci = int(msk2, 2)
        msk3_deci = int(msk3, 2)
        msk4_deci = int(msk4, 2)

        result = str(msk1_deci) + '.' + str(msk2_deci) + '.' + str(msk3_deci) + '.' + str(msk4_deci)
        return result


class Ipv6_range:
    def ipv6_add(self, ip):
        """ IPv6的地址和掩码转换为地址范围 """
        # ip = '2409:8000::4808:1741'
        if '::' in ip:
            # print(ip.split(':'))
            if ip[-2:] == '::':
                numb = len(ip.split(':')) - 2
                add = ':0' * (8 - numb)
            else:
                numb = len(ip.split(':')) - 1
                add = ':0' * (8 - numb) + ':'

            ip_add_0 = ip.replace('::', add)
            ip = ip_add_0
        return ip

    def msk_trans(self, digit):
        add = 128 - int(digit)
        msk_str_b = '1' * int(digit) + '0' * add
        msk1 = msk_str_b[0:16]
        msk2 = msk_str_b[16:32]
        msk3 = msk_str_b[32:48]
        msk4 = msk_str_b[48:64]
        msk5 = msk_str_b[64:80]
        msk6 = msk_str_b[80:96]
        msk7 = msk_str_b[96:112]
        msk8 = msk_str_b[112:128]

        msk1_deci = int(msk1, 2)
        msk2_deci = int(msk2, 2)
        msk3_deci = int(msk3, 2)
        msk4_deci = int(msk4, 2)
        msk5_deci = int(msk5, 2)
        msk6_deci = int(msk6, 2)
        msk7_deci = int(msk7, 2)
        msk8_deci = int(msk8, 2)

        result = str(msk1_deci) + '.' + str(msk2_deci) + '.' + str(msk3_deci) + '.' + str(msk4_deci) + '.' + \
                 str(msk5_deci) + '.' + str(msk6_deci) + '.' + str(msk7_deci) + '.' + str(msk8_deci)

        return result

    def part(self, part_ip, part_mask):
        part_ip = int(part_ip, 16)
        part_mask = int(part_mask)
        delta = 65535 - part_mask

        ip_min = part_ip & part_mask
        ip_max = ip_min + delta

        s_ip_min = str(hex(ip_min)).removeprefix('0x')
        s_ip_max = str(hex(ip_max)).removeprefix('0x')

        return s_ip_min, s_ip_max

    def ips(self, ip_mask):
        sep = ip_mask.split('/')
        ip = sep[0]
        ip = self.ipv6_add(ip)
        mask = self.msk_trans(sep[1])
        return self.ip(ip, mask)

    def ip(self, ip, mask):
        part_ips = ip.split(':')
        part_masks = mask.split('.')
        ip_min = ''
        ip_max = ''
        for i in range(0, 8):
            part_min, part_max = self.part(part_ips[i], part_masks[i])
            ip_min += str(part_min) + ':'
            ip_max += str(part_max) + ':'
        ip_min = ip_min[:-1]
        ip_max = ip_max[:-1]
        return ([ip_min, ip_max])


def Ipv4ToInt(ip: str):
    # 1.将IP地址转换成32位的二进制。
    s = ip.split('.')
    h = []
    g = []
    for temp in s:
        while 0 != temp:
            temp = int(temp)
            a = temp % 2
            h.insert(0, a)
            temp = temp / 2
        if len(h) != 8:
            for i in range(8 - len(h)):
                h.insert(0, 0)
        g.extend(h)
        h = []
    # 2. 将二进制换算成整数：
    res = 0
    j = 0
    for temp2 in g:
        res = res + temp2 * (2 ** (31 - j))
        j += 1
    return res


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
        f.write('\n')


if __name__ == '__main__':
    # add_github_host()  # 添加 github 地址映射
    # ips = Ipv4_range()
    # print(ips.ips('10.90.3.1/30'))
    # print(ips.ip('10.90.3.0', '255.255.255.230'))
    print(Ipv4ToInt('10.9.3.100'))
    print('end...')
