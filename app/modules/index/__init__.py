#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Author:Dreamer
# Time:2018.6.1
from flask import Blueprint


# 1.创建蓝图
index_bp = Blueprint("index",__name__)


# 2.切记：让index模块知道有view.py这个文件
from . import view