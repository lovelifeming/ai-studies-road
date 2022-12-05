#基于的基础镜像。构建特殊镜像，首先需要自己单独构建包含特殊环境的基础镜像，再以基础镜像打包特殊的任务。
FROM python:3.6
#指定作者信息
MAINTAINER zsm
#数据卷信息
VOLUME /tmp

#代码添加到code文件夹
ADD ./scrapy_demo /scrapy_demo
COPY . $BUILD_HOME
ENV BUILD_HOME /scrapy_demo
# 设置code文件夹是工作目录
WORKDIR $BUILD_HOME
ENV LANG C.UTF-8
#暴露容器端口
EXPOSE 8080 5000 6800
# 安装支持
RUN pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple/
RUN chmod 777 /scrapy_probe/start.sh
#ENTRYPOINT 为容器启动后执行的命令
ENTRYPOINT ["python", "/scrapy_demo/start.sh"]

### 构建镜像
## Dockerfilepath：Dockerfile 所在文件夹名称，当前目录为 “.”
#docker build -t imagename Dockerfilepath

## -t参数后，镜像名字:版本。最后有一个 . 是指在当前的目录下去寻找Dockerfile文件
#docker build -t imagename:0.01 .
#docker image ls        #查看系统镜像