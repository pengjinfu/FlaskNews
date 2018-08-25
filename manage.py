#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Author:Dreamer
# Time:2018.6.1
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




app = Flask(__name__)
app.config.from_object(Config)


@app.route('/')
def index():
    return "index"


if __name__ == '__main__':
    app.run()

