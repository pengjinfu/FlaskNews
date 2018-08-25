#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Author:Dreamer
# Time:2018.6.1
from flask import Flask



app = Flask(__name__)



@app.route('/')
def index():
    return "index"


if __name__ == '__main__':
    app.run()

