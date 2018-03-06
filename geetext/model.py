from geetext import db




class User(db.Model):
    '''
    用户
    '''
    __tablename__='user'
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    username=db.Column(db.String(80),unique=True)
    password=db.Column(db.String(32))
    salt=db.Column(db.String(32))


    def __init__(self,username,password,salt=''):
        self.username=username
        self.password=password
        self.salt=salt

    def __repr__(self):
        return '[User %d %s]' % (self.id, self.username)
