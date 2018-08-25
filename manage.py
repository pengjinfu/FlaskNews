#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Author:Dreamer
# Time:2018.6.1
import redis
from redis import StrictRedis
from flask import Flask

import pymysql
pymysql.install_as_MySQLdb()
from flask_sqlalchemy import SQLAlchemy


# 定义配置类
class Config(object):
    """工程配置类"""
    # 开启debug模式
    DEBUG = True

    # 设置mysql数据库
    # 设置mysql数据库的连接
    SQLALCHEMY_DATABASE_URI = "mysql://root:mysql@127.0.0.1:3306/information"
    # 接连之前必须创建一个information数据库，否则会报错

    # 关闭数据库的跟踪模式
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # 设置redis数据库
    # 设置redis的主机地址
    REDIS_HOST = "127.0.0.1"
    # 设置redis的端口
    REDIS_PORT= 6379
    # 设置redis使用哪个空间
    REDIS_NUM  = 1





# 1.创建flask对错
app = Flask(__name__)
# 2.把配置类注册到app里
app.config.from_object(Config)
# 3.创建mysql数据库对象
db = SQLAlchemy(app)
# 4.创建redis对象
redis_store = redis.StrictRedis(host=Config.REDIS_HOST, port=Config.REDIS_PORT,db=Config.REDIS_NUM)

@app.route('/')
def index():
    return "index"


if __name__ == '__main__':
    app.run()

