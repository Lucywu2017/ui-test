# -*- coding: utf-8 -*-

import datetime
from sqlalchemy import Column, Integer, String
from sqlalchemy.engine import create_engine
from CommonLibrary.Util import parse_config
import sqlalchemy
import sqlalchemy.orm
import sqlalchemy.ext.declarative

# 解析配置文件
# config = parse_config()
# 与数据库建立链接
# engine = create_engine('mysql+pymysql://%s:%s@%s/%s?charset=%s' % (
#     config.get('common', 'user'),
#     config.get('common', 'pwd'),
#     config.get('common', 'host'),
#     config.get('common', 'database'),
#     config.get('common', 'charset')), echo=True)
engine = create_engine("mysql+pymysql://root:jZCLftXDUZrCwT95@192.168.1.158/zidonghua", encoding="utf8", echo=False)
with engine.connect() as conn:
    # 最基础的用法
    result = conn.execute("select * from wb_users limit 10;")
    for item in result:
        print(item)

# 首先需要生成一个BaseModel类,作为所有模型类的基类
BaseModel = sqlalchemy.ext.declarative.declarative_base()

# 构建数据模型User
class Users(BaseModel):
    __tablename__ = 'wb_users'
    __table_args__ = {

        "mysql_engine": "InnoDB",  # 表的引擎
        "mysql_charset": "utf8",  # 表的编码格式
    }
    id = Column(Integer, primary_key=True)
    mobile = Column(String)

# 构建数据模型Role
class UsersInfo(BaseModel):
    __tablename__ = 'wb_users_info'
    __table_args__ = {
        "mysql_engine": "InnoDB",  # 表的引擎
        "mysql_charset": "utf8",  # 表的编码格式
    }
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)


# 利用Session对象连接数据库
DBSessinon = sqlalchemy.orm.sessionmaker(bind=engine)   # 创建会话类
session = DBSessinon()                                  # 创建会话对象

# 删除所有表
# BaseModel.metadata.drop_all(engine)
# 创建所有表,如果表已经存在,则不会创建
BaseModel.metadata.create_all(engine)

