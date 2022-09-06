import os
import json
import configparser


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
