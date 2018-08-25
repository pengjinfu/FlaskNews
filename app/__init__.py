#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Author:Dreamer
# Time:2018.6.1
import redis
from flask import Flask

from flask_session import Session

from flask_wtf.csrf import CSRFProtect

import pymysql
pymysql.install_as_MySQLdb()

from flask_sqlalchemy import SQLAlchemy

from config import config_dict

#  外界使用方式:  create_app("development") --> 开发模式的app
#              create_app("production")  --> 线上模式的app
def create_app(config_name):
    """生产app的工厂方法"""
    # 1.创建flask对错
    app = Flask(__name__)
    # 2.把配置类注册到app里
    ConfigClass = config_dict[config_name]
    app.config.from_object(ConfigClass)
    # 3.创建mysql数据库对象
    db = SQLAlchemy(app)
    # 4.创建redis对象
    redis_store = redis.StrictRedis(host=ConfigClass.REDIS_HOST, port=ConfigClass.REDIS_PORT,db=ConfigClass.REDIS_NUM)
    # 5. 开启csrf后端保护验证机制
    # 提取cookie中的csrf_token和ajax请求头里面csrf_token进行比较验证操作
    csrf = CSRFProtect(app)   # session不由表单携带而是放在redis数据库里，这里为什么要这样是个大知识点
    # 6.创建session拓展类的对象(将session的存储调整到redis中)
    Session(app)
