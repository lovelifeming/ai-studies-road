docker部署 scrapyd + scrapydweb：

创建镜像并启动

docker run -tid --net=host --name scrapy_demo -e LANG="C.UTF-8" scrapy_demo:latest python /start.sh /bin/bash

修改上传代码后在 scrapy.cfg 配置文件同级目录 部署构建项目：
scrapyd-deploy spiderName  -p projectName

再在webui上面发布最新版本



生成环境依赖包：
$pip freeze > requirements.txt
生成项目依赖包：
$pip install  pipreqs
$pipreqs ./ –encoding=utf8 > requirements.txt		#在项目根目录执行

安装环境依赖包：
$pip install -r requirements.txt