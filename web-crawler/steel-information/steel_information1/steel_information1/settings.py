# Scrapy settings for steel_information1 project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html
# Scrapy项目的名字,这将用来构造默认 User-Agent,同时也用来log,当您使用 startproject 命令创建项目时其也被自动赋值。
BOT_NAME = 'steel_information1'
# Scrapy搜索spider的模块列表 默认: [xxx.spiders]
SPIDER_MODULES = ['steel_information1.spiders']
# 使用 genspider 命令创建新spider的模块。默认: 'xxx.spiders'
NEWSPIDER_MODULE = 'steel_information1.spiders'

COMMANDS_MODULE = 'steel_information1.commands'

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
DOWNLOAD_DELAY = 4
# The download delay setting will honor only one of:
# 下载延迟设置，只能有一个生效
# CONCURRENT_REQUESTS_PER_DOMAIN = 16    # 对单个网站进行并发请求的最大值
CONCURRENT_REQUESTS_PER_IP = 4
# 对单个ip进行并发请求的最大值，如果非0，则忽略，CONCURRENT_REQUESTS_PER_DOMAIN 设定,使用该设定。
# 也就是说,并发限制将针对IP,而不是网站。该设定也影响 DOWNLOAD_DELAY: 如果 CONCURRENT_REQUESTS_PER_IP 非0,下载延迟应用在IP而不是网站上。

# Disable cookies (enabled by default)
# 禁用cookie（默认情况下启用）
# COOKIES_ENABLED = False

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

# Enable or disable spider middlewares
# 启用或禁用蜘蛛中间件
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'steel_information1.middlewares.SteelInformationSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# 启用或禁用下载器中间件
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    'steel_information1.middlewares.SteelInformation1DownloaderMiddleware': 543,
}

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
    'steel_information1.pipelines.SteelInfo1Item': 300,
    'steel_information1.pipelines.SaveImagePipeline': 500,
}

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
# 启用或配置 Http 缓存（默认情况下禁用）
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

# -----------------------日志文件配置-----------------------------------
# # 默认: True,是否启用logging。
# LOG_ENABLED = True
# # 默认: 'utf-8',logging使用的编码。
# LOG_ENCODING = 'utf-8'
# # 它是利用它的日志信息可以被格式化的字符串。默认值：'%(asctime)s [%(name)s] %(levelname)s: %(message)s'
# LOG_FORMAT = '%(asctime)s [%(name)s] %(levelname)s: %(message)s'
# # 它是利用它的日期/时间可以格式化字符串。默认值： '%Y-%m-%d %H:%M:%S'
# LOG_DATEFORMAT = '%Y-%m-%d %H:%M:%S'
# # 日志文件名
# LOG_FILE = "steel_information1.log"
# # 日志文件级别,默认值：“DEBUG”,log的最低级别。可选的级别有: CRITICAL、 ERROR、WARNING、INFO、DEBUG 。
# LOG_LEVEL = 'WARNING'

# 导出爬取数据配置
# FEED_FORMAT = 'json'
# FEED_URL = 'file_name_%(name)s_%(time)s.json'

# MySQL配置
MYSQL_DB_NAME = 'test_db'
MYSQL_HOST = '192.168.1.100'
MYSQL_PORT = 3306
MYSQL_USER = 'root'
MYSQL_PASSWORD = '123456'
STEEL_KEYWORD = '废钢|铁矿石|热轧板卷|热卷|冷轧板卷|冷轧|中厚板|高线|盘螺|螺纹钢|焦煤|焦炭|型钢|钢管|带钢|涂镀|硅钢|' \
                '钢坯|水泥|混凝土|优特钢|工业线材|西南热卷库存|西南冷轧库存|西南螺纹钢库存|西南建材库存|挖掘机|冰箱|' \
                '彩电|洗衣机|汽车销量|房地产|汽车产量|CPI|PMI|限产|中钢协|棚改|中汽协|攀钢|重钢|威钢|德胜|成实|昆钢|' \
                '水钢|达钢|龙钢|陕钢|建龙|玉昆|宝钢|首钢|鞍钢|河钢|沙钢'
METAL_KEYWORD = '铜|铜矿|电解铜|铝|铝土矿|铅|铅锌矿|锌|镍|镍矿|电解镍|硫酸镍|基本金属|铁合金|稀土|钴|锂|石墨|碳素|' \
                '钽铌|锆|锑|镁|汞|铟|铋|锗|碲|镓|硒|铍|镉|砷|铼|矿业|贵金属|金|银|钯|铂|耐材|不锈钢|钨|钼|钒|钛|铬|' \
                '锰|硅|硅铁|硅锰|锂电池|汽车|新能源汽车'
