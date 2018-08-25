#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Author:Dreamer
# Time:2018.6.1
from flask import Flask




# 定义配置类
class Config(object):
    """工程配置类"""
    # 开启debug模式
    DEBUG = True



app = Flask(__name__)



@app.route('/')
def index():
    return "index"


if __name__ == '__main__':
    app.run()

