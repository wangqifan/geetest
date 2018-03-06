from geetext import app,db
from geetext.model import User
from flask import request,make_response,jsonify
import random,hashlib,uuid
from geetext.redis  import setsession,delay3day,getuserfromRedis,deletesession,findkey
import uuid



#
#注册接口
#
@app.route('/reg/',methods={'post','get'})
def reg():
    username=request.values.get('username').strip()
    password=request.values.get('password').strip()

    if username=='' or password=='':
        return jsonify({"success":False,"message":"用户名或密码为空"})

    if User.query.filter_by(username=username).first() is not None:
        return jsonify({"success":False,"message":"用户名已经存在"})

    try:
        salt = '.'.join(random.sample('01234567890abcdefghigABCDEFGHI', 10))
        m = hashlib.md5()
        m.update((password + salt).encode("utf-8"))
        password = m.hexdigest()
        user = User(username, password, salt)
        db.session.add(user)
        db.session.commit()
        return jsonify({"success":True,"message":"注册成功"})
    except:
        return jsonify({"success":False,"message":"注册失败，请重试"})



#
#登录接口
#
@app.route('/login/',methods={'get','post'})
def login():
    username = request.values.get('username').strip()
    password = request.values.get('password').strip()

    if username == '' or password == '':
        return jsonify({"success": False, "message": "用户名或密码不能为空"})

    user = User.query.filter_by(username=username).first()
    if user is None:
        return  jsonify({"success":False,"message":"用户名不存在"})

    m = hashlib.md5()
    m.update((password + user.salt).encode('utf-8'))
    if (m.hexdigest() != user.password):
        return jsonify({"success":False,"message":"密码错误"})

    token=uuid.uuid1().hex
    print(type(token),token)
    print(token)
    respone=make_response(jsonify({"success": True, "message": "登录成功"}))
    respone.set_cookie('user',token)
    setsession(token,user.username)
    return respone





#
#获取登录用户
#
@app.route('/user/',methods={'post','get'})
def getuser():
    token=request.cookies.get('user')
    if token is None:
        return jsonify({"success": False, "message": "没有登陆"})
    print(token)
    username=getuserfromRedis(token)
    if username is None:
        return jsonify({"success": False, "message": "请重新登陆"})
    user=User.query.filter_by(username=username).first()
    if user is None:
        return jsonify({"success": False, "message": "未找到用户信息"})
    return jsonify({"success":True,"message":user.__repr__()})




#
#登出
#
@app.route('/layout/',methods={'post','get'})
def layout():
    token = request.cookies.get('user')
    deletesession(token)
    if findkey(token):
        return jsonify({"success": False, "message": "登出失败"})
    else:
        return jsonify({"success":True,"message":"登出成功"})



#
#修改密码
#
@app.route('/changepassword/',methods={'post','get'})
def changepassword():

    password = request.values.get('password').strip()
    try:
        token = request.cookies.get('user')
        username = getuserfromRedis(token)
        user = User.query.filter_by(username=username).first()
        m = hashlib.md5()
        m.update((password + user.salt).encode("utf-8"))
        password = m.hexdigest()
        user.password=password
        db.session.commit()
        return jsonify({"success":True,"message":"修改密码成功"})
    except:
        return jsonify({"success":True,"message":"修改密码失败"})















