#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Author:Dreamer
# Time:2018.6.1
import redis
from redis import StrictRedis
from flask import Flask

from flask_session import Session

from flask_wtf.csrf import CSRFProtect
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

    # 设置加密字符串
    SECRET_KEY ="/W73UULUS4UFO5omviuVZz6+Bcjs5+2nRdvmyYNq1wEryZsMeluALSDGxGnuYoKX""
    # 调整session存储的位置（存储到redis里）
    # 以下的配置均可在Session的源码看到，或者可以找到官网查询

    # 指明session存储到哪种数据库
    SESSION_TYPE = "redis"
    # 上面的指明的数据库的实例对象
    SESSION_REDIS = StrictRedis(host=REDIS_HOST, port=REDIS_PORT, db=REDIS_NUM)
    # session数据需要加密
    SESSION_USE_SIGNER = True
    # 不设置永久存储
    SESSION_PERMANENT = False
    # 默认存储的有效时长 （没有调整之前默认值是timedelta(days=31)）
    PERMANENT_SESSION_LIFETIME = 86400 * 2





# 1.创建flask对错
app = Flask(__name__)
# 2.把配置类注册到app里
app.config.from_object(Config)
# 3.创建mysql数据库对象
db = SQLAlchemy(app)
# 4.创建redis对象
redis_store = redis.StrictRedis(host=Config.REDIS_HOST, port=Config.REDIS_PORT,db=Config.REDIS_NUM)
# 5. 开启csrf后端保护验证机制
# 提取cookie中的csrf_token和ajax请求头里面csrf_token进行比较验证操作
csrf = CSRFProtect(app)   # session不由表单携带而是放在redis数据库里，这里为什么要这样是个大知识点
# 6.创建session拓展类的对象(将session的存储调整到redis中)
Session(app)


@app.route('/')
def index():
    return "index"


if __name__ == '__main__':
    app.run()

