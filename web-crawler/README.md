#  web crawler  网络爬虫

Scrapy框架 
中文官方主页：https://scrapy-chs.readthedocs.io/zh_CN/latest/index.html
可以通过对接Portia 实现可视化配置
文件目录：
scrapy.cfg：项目的总配置文件，通常无须修改。
picture-spider：项目的 Python 模块，程序将从此处导入 Python 代码。
picture-spider/items.py：用于定义项目用到的 Item 类。Item 类就是一个 DTO（数据传输对象），通常就是定义 N 个属性，该类需要由开发者来定义。
picture-spider/pipelines.py：项目的管道文件，它负责处理爬取到的信息。该文件需要由开发者编写。
picture-spider/settings.py：项目的配置文件，在该文件中进行项目相关配置。
picture-spider/spiders：在该目录下存放项目所需的蜘蛛，蜘蛛负责抓取项目感兴趣的信息。
items.py: 用来存放爬虫爬取下来数据的模型
middlewares.py: 用来存放各种中间件的文件
scrapy.cfg: 项目的配置文件


PySpider框架
中文官方主页：http://docs.pyspider.org/en/latest/

提供了方便易用的 WebUi 系统，可视化的编写和调试爬虫
提供爬去进度监控 / 爬去结果查看 / 爬虫项目管理等功能
支持多种后端数据库，如：MySQL / MongoDB / Rides 等
支持多种消息队列，如：RabbimMQ / Beanstalk / Redis / Kombu
提供优先级控制 / 失败重试 / 定时抓取等
对接了PhantonJS。可以抓取Javascript 渲染的页面
支持单机和分布式部署，支持 Docker 部署
