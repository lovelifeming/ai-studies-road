# Scrapy settings for scrapy_demo project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html
# Scrapy项目的名字,这将用来构造默认 User-Agent,同时也用来log,当您使用 startproject 命令创建项目时其也被自动赋值。
import os
from datetime import datetime

BOT_NAME = 'scrapy_demo'
# Scrapy搜索spider的模块列表 默认: [xxx.spiders]
SPIDER_MODULES = ['scrapy_demo.spiders']
# 使用 genspider 命令创建新spider的模块。默认: 'xxx.spiders'
NEWSPIDER_MODULE = 'scrapy_demo.spiders'

COMMANDS_MODULE = 'scrapy_demo.commands'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# 爬取的默认User-Agent，除非被覆盖
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'

# Obey robots.txt rules
# 如果启用,Scrapy将会采用 robots.txt 策略，常使用不遵循 False
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# Scrapy downloader 并发请求(concurrent requests)的最大值,默认: 16
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# 未同意网站的请求配置延迟（默认为0）
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# 下载器延迟时间，下载器在同一网站面前需要等待的时间，该选项可以用来限制爬取速度,减轻服务器压力。同时也支持小数:0.25 以秒为单
DOWNLOAD_DELAY = 1
DOWNLOAD_TIMEOUT = 60
RANDOMIZE_DOWNLOAD_DELAY = True
# The download delay setting will honor only one of:
# 下载延迟设置，只能有一个生效
# CONCURRENT_REQUESTS_PER_DOMAIN = 16    # 对单个网站进行并发请求的最大值
CONCURRENT_REQUESTS_PER_IP = 16
# 对单个ip进行并发请求的最大值，如果非0，则忽略，CONCURRENT_REQUESTS_PER_DOMAIN 设定,使用该设定。
# 也就是说,并发限制将针对IP,而不是网站。该设定也影响 DOWNLOAD_DELAY: 如果 CONCURRENT_REQUESTS_PER_IP 非0,下载延迟应用在IP而不是网站上。

# Disable cookies (enabled by default)
# 禁用cookie（默认情况下启用） 当COOKIES_ENABLED是注释的时候，scrapy默认没有开启cookie
## 当COOKIES_ENABLED没有注释设置为False的时候，scrapy默认使用了settings里面的cookie
## 当COOKIES_ENABLED设置为True的时候，scrapy就会把settings的cookie关掉，使用自定义cookie
# COOKIES_ENABLED = False    #如果使用自定义cookie就把COOKIES_ENABLED设置为True，如果使用settings的cookie就把COOKIES_ENABLED设置为False
# 打印cookie信息
# COOKIES_DEBUG = True

# Disable Telnet Console (enabled by default)
# 禁用Telent控制台（默认启用）
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# 覆盖默认请求标头，也可以加入请求头，获取同样来自开发着工具，
# 很多网站都会检查客户端的headers，比如豆瓣就是每一个请求都检查headers的user_agent，否则只会返回403，可以开启 USER_AGENT 请求头
DEFAULT_REQUEST_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en',
    'User_Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
}
COMMON_USER_AGENT = [
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)',
    'Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
    'Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)',
    'Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)',
    'Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)',
    'Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)',
    'Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6',
    'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1',
    'Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0',
    'Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5',
    'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20',
    'Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52',
    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)',
    'Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
    'Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)',
    'Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)',
    'Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)',
    'Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)',
    'Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6',
    'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1',
    'Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0',
    'Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5',
    'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20',
    'Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/2.0 Safari/536.11',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; LBBROWSER)',
    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E; LBBROWSER)',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 LBBROWSER',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; QQBrowser/7.0.3698.400)',
    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; 360SE)',
    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)',
    'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1',
    'Mozilla/5.0 (iPad; U; CPU OS 4_2_1 like Mac OS X; zh-cn) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148 Safari/6533.18.5',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0b13pre) Gecko/20110307 Firefox/4.0b13pre',
    'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:16.0) Gecko/20100101 Firefox/16.0',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
    'Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    # ie
    'Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)',
    # msie
    'Mozilla/5.0 (compatible; MSIE 10.0; Macintosh; Intel Mac OS X 10_7_3; Trident/6.0)',
    # 'Internet Explorer'
    'Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0; GTB7.4; InfoPath.2; SV1; .NET CLR 3.3.69573; WOW64; en-US)',
    # opera
    'Opera/9.80 (X11; Linux i686; U; ru) Presto/2.8.131 Version/11.11',
    # chrome
    'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.2 (KHTML, like Gecko) Chrome/22.0.1216.0 Safari/537.2',
    # google
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_4) AppleWebKit/537.13 (KHTML, like Gecko) Chrome/24.0.1290.1 Safari/537.13',
    # 'google chrome'
    'Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11',
    # Ubuntu
    'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:15.0) Gecko/20100101 Firefox/15.0.1',
    # Mac safari
    'Mozilla/5.0 (iPad; CPU OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5355d Safari/8536.25',
    # Firefox版
    'Mozilla/5.0 (Windows NT 6.2; Win64; x64; rv:16.0.1) Gecko/20121011 Firefox/21.0.1',
    'Mozilla/5.0 (Windows NT 6.2; Win64; x64; rv:16.0.1) Gecko/20121011 Firefox/16.0.1'
]

# Enable or disable spider middlewares
# 启用或禁用蜘蛛中间件
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html[小程序]202009月积微大数据部门物资申请清单表
# SPIDER_MIDDLEWARES = {
#    'scrapy_demo.middlewares.ScrapyDemoSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# 启用或禁用下载器中间件
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    'scrapy_demo.middlewares.ScrapyDemoSpiderMiddleware': 543,
}
# DOWNLOADER_STATS = False
# Enable or disable extensions
# 启用或禁用扩展程序
# See https://docs.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# 配置项目管道，如下载图片的图片管道，分布式爬虫多爬虫的pipeline，结尾int值是优先级，可以理解为权重，以逗号间隔，是个集合
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'scrapy_demo.pipelinesimage.PipelineImages': 1,
    'scrapy_demo.pipelinespymysql.PipelineMySql': 300
}
IMAGES_URLS_FIELD = "images_urls"  # images_urls 是在items.py中配置的网络爬取得图片地址
# 配置保存本地的地址
project_dir = os.path.abspath(os.path.dirname(__file__))  # 获取当前爬虫项目的绝对路径
# IMAGES_STORE = os.path.join(project_dir, 'images')  # 组装新的图片路径
IMAGES_STORE = './image/'
# Enable and configure the AutoThrottle extension (disabled by default)
# 启用或配置AutoThrottle扩展（默认情况下禁用）
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# 初始下载延迟
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# 在高延迟的情况下设置最大下载延迟
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# Scrapy请求的平均数量应该并行发送每个远程服务器
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# 启用显示所收到的每个响应的调节统计信息
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# 启用或配置 Http 缓存（默认情况下禁用），会导致不发送请求，一直处理缓存中的数据
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

# 是否启用内存使用插件。当Scrapy进程占用的内存超出限制时，该插件将会关闭Scrapy进程， 同时发送email进行通知。
# MEMUSAGE_ENABLED = False
# # # 在关闭Scrapy之前所允许的最大内存数，如果为0，将不做限制。
# # MEMUSAGE_LIMIT_MB = 0
# # # 达到内存限制时通知的email列表
# # MEMUSAGE_NOTIFY_MAIL = False
# # # 每个spider被关闭时是否发送内存使用报告
# # MEMUSAGE_REPORT = False
# # # 在发送警告email前所允许的最大内存数(单位: MB)(如果 MEMUSAGE_ENABLED为True)。 如果为0，将不发送警告。
# # MEMUSAGE_WARNING_MB = 0

# -----------------------日志文件配置-----------------------------------
# # 默认: True,是否启用logging。
LOG_ENABLED = True
# # 默认: 'utf-8',logging使用的编码。
LOG_ENCODING = 'utf-8'
# # 它是利用它的日志信息可以被格式化的字符串。默认值：'%(asctime)s [%(name)s] %(levelname)s: %(message)s'
LOG_FORMAT = '%(asctime)s [%(name)s] %(levelname)s: %(message)s'
# # 它是利用它的日期/时间可以格式化字符串。默认值： '%Y-%m-%d %H:%M:%S'
LOG_DATEFORMAT = '%Y-%m-%d %H:%M:%S'
# # 日志文件名
to_day = datetime.now().date().__str__()
LOG_FILE_PATH = './logs/scrapy_demo_{}.log'.format(to_day)
LOG_FILE = LOG_FILE_PATH
# # 日志文件级别,默认值：“DEBUG”,log的最低级别。可选的级别有: CRITICAL、 ERROR、WARNING、INFO、DEBUG 。
# LOG_LEVEL = 'INFO'

# 导出爬取数据配置
# FEED_FORMAT = 'json'
# FEED_URL = 'file_name_%(name)s_%(time)s.json'

# MySQL配置
MYSQL_DB_NAME = 'test_db'
MYSQL_HOST = '127.0.0.1'
MYSQL_PORT = 3306
MYSQL_USER = 'root'
MYSQL_PASSWORD = '123456'

# ES 配置
ES_HOSTS = ['127.0.0.1']
ES_USER = 'root'
ES_PASSWORD = '123456'
ES_PORT = 9201
