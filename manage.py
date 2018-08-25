#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Author:Dreamer
# Time:2018.6.1
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from app import create_app,db


# 单一职责的原则：manage.py 仅仅作为项目启动文件即可
# 工厂方法的调用（ofo公司）
app = create_app("development")

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

