import redis
from geetext import app

HOST=app.config["REDISHOST"]
PORT=app.config["REDISPORT"]
pool = redis.ConnectionPool(host=HOST, port=PORT,decode_responses=True)
r = redis.Redis(connection_pool=pool)
expiretime=60*10*24*3


def setsession(token,username):
    return r.set(name=token,value=username,ex=expiretime)



def delay3day(token):
    r.setex(token,expiretime)



def getuserfromRedis(token):
    return r.get(name=token)



def deletesession(token):
    return   r.delete(token)

def findkey(token):
    return r.exists(token)
