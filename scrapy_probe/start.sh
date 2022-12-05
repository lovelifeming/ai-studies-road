#! /bin/bash
#sudo su
source /root/anaconda3/bin/activate python6
echo 'scrapy start ...'
cd /opt/crawl_web/scrapy_demo/scrapy_demo/
scrapy crawlall  2>> error_log.log
