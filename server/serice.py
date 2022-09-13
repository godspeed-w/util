import util as ut
from bottle import Bottle, request
import json


app = Bottle()
@app.route('/')
def index():
    '''设置主路由为登陆页'''
    return '''<h1>这是主页</h1>'''


@app.route('/getAllUsers', method='get')
def getAllUsers():
    '''查询所有'''
    res = ut.dbExcute("select * from user")
    return json.dumps(res)


@app.route('/getUserById', method='get')
def getUserById():
    '''通过id查询'''
    uid = request.query.id
    res = ut.dbExcute("select * from user where id = {}".format(uid))
    return json.dumps(res)


@app.route('/addUser', method='post')
def addUser():
    '''新增用户, json请求'''
    data = json.load(request.body)
    uid, name, age = data['id'], data['name'], data['age']
    res = ut.dbExcuteCommit(
        "insert into user values ({},{},{})".format(uid, name, age))
    return json.dumps(res)


@app.route('/updateUser', method='post')
def addUser():
    '''更新用户, json请求'''
    data = json.load(request.body)
    uid, name, age = data['id'], data['name'], data['age']
    res = ut.dbExcuteCommit(
        "update user set name={}, age={} where id={}".format(name, age, uid))
    return json.dumps(res)


@app.route('/deleteUserById', method='get')
def getUserById():
    '''删除用户,通过ID'''
    uid = request.query.id
    res = ut.dbExcuteCommit("delete from user where id = {}".format(uid))
    return json.dumps(res)


app.run(host='localhost', port=8080)
