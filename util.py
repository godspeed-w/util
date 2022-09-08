import pymysql
import cx_Oracle
import os
import json
import configparser


def makelist(data=None):
    """好用的创建list工具"""
    if isinstance(data, (tuple, list, set, dict)):
        return list(data)
    elif data:
        return [data]
    else:
        return []

########################################
# 文件操作工具
########################################


def getConf(iniFile=None):
    """获取ini配置文件参数"""
    con = configparser.ConfigParser()
    con.read(iniFile, encoding='utf-8')
    env = dict(con.items('active'))['env']
    actEnv = dict(con.items(env))
    return actEnv


def readFile(fileName=None):
    """读文件返回文件指针"""
    file = None
    try:
        open(fileName, 'r', encoding='utf-8').readlines()
    except:
        file = open(fileName, 'r', encoding='gbk')
    else:
        file = open(fileName, 'r', encoding='utf-8')
    return file


def readFile2Lines(fileName=None, useStrip=True):
    """读文件返回行列表，可选择去掉\\n后缀"""
    f = readFile(fileName)
    lines = f.readlines()
    if useStrip:
        lines = [i.strip() for i in lines]
    return lines


def readJsonFile(fileName=None):
    """读json文件"""
    fp = readFile(fileName)
    return json.load(fp)


########################################
# 数据库工具
########################################


def dbExcute(execSql=''):
    """执行数据库操作"""
    config = {
        'host': '127.0.0.1',
        'port': 3306,
        'user': 'root',
        'password': '12345678',
        'database': 'springboot',
        'charset': 'utf8'
    }
    db = pymysql.connect(**config)
    cursor = db.cursor()
    cursor.execute(execSql)
    data = cursor.fetchall()
    db.close()
    return data
