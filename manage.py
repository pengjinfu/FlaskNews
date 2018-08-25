#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Author:Dreamer
# Time:2018.6.1
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from app import app,db

# 7. 创建manager管理类
manager = Manager(app)
# 初始化迁移对象
Migrate(app, db)
# 将迁移命令添加到管理对象中
manager.add_command("db", MigrateCommand)

@app.route('/')
def index():
    return "index"


if __name__ == '__main__':
    # python manage.py runserver -p -h
    manager.run()

