# docker部署 scrapyd + scrapydweb：

创建镜像并启动

docker run -tid --net=host --name scrapy_demo -e LANG="C.UTF-8" scrapy_demo:latest python /start.sh /bin/bash

修改上传代码后在 scrapy.cfg 配置文件同级目录 部署构建项目：
scrapyd-deploy spiderName  -p projectName

再在webui上面发布最新版本


# 生成环境依赖包：
$pip freeze > requirements.txt
生成项目依赖包：
$pip install  pipreqs
$pipreqs ./ –encoding=utf8 > requirements.txt		#在项目根目录执行

安装环境依赖包：
$pip install -r requirements.txt

# scrapy 爬取技巧：
start_requests()    自定义起始爬取网页，方便爬取前的操作。
yield item  提交给管道文件处理 pipelines
yield scrapy.Request( next_url, callback=self.parse)   提交子请求，回调递归处理
response.urljoin()   拼凑成绝对网址
scrapy.FormRequest(url=url, formdata=data, callback=self.parse) post请求
images_urls 是在items.py中配置的网络爬取得图片地址

网站爬取规则：robots.txt
# *代表任意字符，匹配 0 或多个任意字符；/代表目录；$代表匹配行结束符；

域名/robots.txt               #查看网站爬取规则，例如：https://www.baidu.com/robots.txt

User-agent: *               #所有代理的爬虫，可以指定爬虫名称，应当遵守如下协议
Allow:/                     #代表可以爬取的内容目录。/ 表示根目录，即所有内容
Disallow:/                  #代表不可爬取的目录。如果是 / 后面没有写内容,便是其对应的访问者不可爬取所有内容
Disallow: /?*               #任何爬虫都不可访问以问号开头的网址
Disallow: /?$               #任何爬虫都不可访问以问号结尾的网址
Disallow: /#$               #任何爬虫都不可访问以 #号结尾的网址
Disallow: /*?*              #禁止爬取网站中所有包含问号 (?) 的网址
Disallow: /.jpg$            #禁止爬取网页所有的 jpg格式的图片
User-agent: EtaoSpider      #指定代理的爬虫名称，EtaoSpider即是一淘爬虫名
