#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Author:Dreamer
# Time:2018.6.1

from . import index_bp

@index_bp.route('/')
def index():
    return "index"