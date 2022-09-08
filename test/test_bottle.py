from bottle import Bottle, request
import json


app = Bottle()
# 设置主路由为登陆页
@app.route('/')
@app.route('/login', method='get')
def login_form():
    return '''<form action="logincheck" method = "POST">
                name <input name="name" type="text" />
                password <input name="password" type="password" />
                <input type="submit" value="Login" />
                </form>'''

@app.route('/logincheck', method = 'POST')
def login():
    name = request.forms.get('name')
    password = request.forms.get('password')
    return "success: {},{}".format(name, password)

# 获取url中带的变量值
# http://localhost:8080/test_get?name=123&pwd=qaz123
@app.route('/test_get', method='get')
def testget():
    name = request.query.name
    pwd = request.query.pwd
    print(name, pwd)
    return "success: {},{}".format(name, pwd)

# 测试接收json类型请求
@app.route('/test_postJson', method='post')
def testPostJson():
    data = json.load(request.body)
    print(data)
    return "res:{}".format(str(data))

app.run(host='localhost', port=8080)
