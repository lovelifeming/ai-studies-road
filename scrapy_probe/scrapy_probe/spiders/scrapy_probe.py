#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/2/1 13:45
# @File : scrapy_probe
import random
import time
import uuid

import scrapy


class DemoSpider(scrapy.Spider):
    name = 'scrapyProbe'
    allowed_domains = ['https://10.130.1.206']
    # start_urls = ['https://10.130.1.206/skyeye/rules/']
    # 配置自定义类 PIPELINES
    custom_settings = {'ITEM_PIPELINES': {'scrapy_probe.pipelines.PipelineImages': 1,
                                          'scrapy_probe.pipelines.PipelineMySql': 300}}

    def start_requests(self):
        """ 开始爬取网页之前的请求 """
        # login_url = 'https://10.130.1.206/skyeye/admin/login'
        # code_url = 'https://10.130.1.206/skyeye/admin/code?r=' + str(random.random())
        # login_resp = scrapy.Request(login_url)
        # ocr = DdddOcr()
        # # 创建未验证的上下文
        # context = ssl._create_unverified_context()
        # # 在url中传入上下文参数
        # urlopen = urllib.request.urlopen(code_url, context=context)
        # img = urlopen.read()
        # code = ocr.classification(img)
        # print(code)
        # uid = uuid.uuid4().__str__().replace('-', '')
        # pw = 'jwwl@tz1-xxaqb'
        # sky = 'skyeyesensor?000'
        # aes = AES.new(str.encode(sky), AES.MODE_ECB)  # 初始化加密器，本例采用ECB加密模式
        # encrypted_text = str(base64.encodebytes(aes.encrypt(add_to_16(pw))), encoding='utf8').replace('\n', '')  # 加密
        #
        # user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) ' \
        #              'Chrome/100.0.4896.88 Safari/537.36'
        # # requests_get = requests.get('https://10.130.1.206/home/rule',verify=False)
        # meta = login_resp.meta
        # # cookie_ = requests_get.headers['Set-Cookie']
        # # csrf1 = requests_get.text.find("csrf-token content")
        # # csrf = requests_get.text[csrf1+ 19:csrf1 + 51]
        # from_data = {'authcode': code,
        #              'csrf_token': csrf,
        #              'password': str(encrypted_text),
        #              'r': str(random.random()),
        #              'username': "admin"}
        # request = scrapy.FormRequest(login_url, cookies={
        #     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        #     'Accept-Encoding': 'gzip, deflate, br',
        #     'Accept-Language': 'zh-CN,zh;q=0.9',
        #     'Cookie': 'session-sensor=' + cookie_,
        #     'Connection': 'keep-alive', 'user-agent': user_agent,
        #     'Host': '10.130.1.206',
        #     'Referer': 'https://10.130.1.206/home/backdoorRule'},
        #                              formdata=from_data)  # callback=self.start_url)
        #
        # updating_url = 'https://10.130.1.206/skyeye/config/is_updating?csrf_token=' + csrf + '&r=' + str(random.random())
        # updating_req = scrapy.Request(updating_url)
        # updating_url = 'https://10.130.1.206/skyeye/admin/login?csrf_token=' + csrf + '&r=' + str(random.random())
        # updating_req1 = scrapy.Request(updating_url)
        # updating_url = 'https://10.130.1.206/skyeye/config/license?dtype=json&csrf_token=' + csrf + '&r=' + str(random.random())
        # updating_req2 = scrapy.Request(updating_url)

        header = {'Accept': '*/*',
                  'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'zh-CN,zh;q=0.9',
                  'Connection': 'keep-alive',
                  'Cookie': "session-sensor=050a5691-7eac-484d-afa4-53c8ac9f5289",
                  'Host': '10.130.1.206',
                  'Referer': 'https://10.130.1.206/home/rule',
                  'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
                  'sec-ch-ua-mobile': '?0',
                  'sec-ch-ua-platform': '"Windows"',
                  'Sec-Fetch-Dest': 'empty',
                  'Sec-Fetch-Mode': 'cors',
                  'Sec-Fetch-Site': 'same-origin',
                  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36',
                  'X-Requested-With': 'XMLHttpRequest'}
        updating_url = 'https://10.130.1.206/skyeye/rules/getRule?rule=&level=all&confidence=1,2,3&category=all&attack_res=0,1,2,3&block=all&state=all&page=1&pagesize=20&order_by=level:0&csrf_token=ef6c5f1d878d15731404ec2d99c89e16&r=' + str(random.random())
        yield scrapy.Request(updating_url, headers=header, callback=self.parse, meta={'dont_redirect': True},
                                       method='GET', dont_filter=True)
        # updating_req3 = Request.get(updating_url,verify=False,headers=header)


    # def start_url(self, response):
        # for ul in self.start_urls:
        #     url = ul
        #     yield scrapy.Request(url, callback=self.parse)

    def parse(self, response):
        """
        start_requests()    自定义起始爬取网页，方便爬取前的操作。
        yield item  提交给管道文件处理 pipelines
        yield scrapy.Request( next_url, callback=self.parse)   提交子请求，回调递归处理
        response.urljoin()   拼凑成绝对网址
        scrapy.FormRequest(url=url, formdata=data, callback=self.parse) post请求
        images_urls 是在items.py中配置的网络爬取得图片地址
        """
        results = response.xpath("//div[contains(@class,'key-list')]//div[@class='item-mod ']")
        print(response.url)
        for it in results:
            # https://10.130.1.206/skyeye/alarm/getBackdoorDetail?id=10000&type=1&csrf_token=3aaa19527706166aa9cd0a721dd718c3&r=0.8106951149784347
            item = {}
            price = it.xpath(".//a[@class='favor-pos']//text()").extract()
            item['price'] = ''.join([i.strip() for i in price])
            item['title'] = it.xpath(".//span[@class='items-name']//text()").extract_first()
            item['address'] = it.xpath(".//span[@class='list-map']//text()").extract_first()
            types = it.xpath(".//a[@class='huxing']//text()").extract()
            for i, val in enumerate(types):
                types[i] = val.strip()
            product_type = ''.join(types)
            item['product_type'] = product_type
            classified = it.xpath(".//div[@class='tag-panel']//text()").getall()
            item['classified'] = ''.join([i.strip() for i in classified])
            source_site = it.xpath(".//a[@class='lp-name']/@href").get()
            item['source_site'] = source_site
            item['unique_key'] = uuid.uuid1().hex if source_site is None \
                else source_site[source_site.rindex('/') + 1:source_site.rindex('.')]
            item["publish_time"] = item["spider_time"] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
            item["city"] = item["area"] = None
            item["version"] = 1
            yield scrapy.Request(response.urljoin(item['source_site']), callback=self.detail_page, cb_kwargs=item)
        next_page = response.xpath("//div[@class='pagination']//a[contains(@class,'next-page')]//@href").extract_first()
        if next_page is not None:
            yield scrapy.Request(next_page, callback=self.parse)

    def detail_page(self, response, **kwargs):
        print(response.url)
        print(kwargs)

        yield kwargs
