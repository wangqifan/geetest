from geetext import app,db
from flask_script import Manager

manager=Manager(app)

@manager.command
def init_datebase():
    db.drop_all()
    db.create_all()


if __name__ == '__main__':
    init_datebase()