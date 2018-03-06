import  unittest

from geetext import app


class geetextclass(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()
        print('setUp')

    def tearDown(self):
        print('teardown')
        pass

    def register(self,username,password):
        return self.app.post('/reg/',data={"username":username, "password":password},follow_redirects=True)

    def login(self, username, password):
        return self.app.post('/login/', data={"username": username, "password": password}, follow_redirects=True)

    def logout(self):
        return self.app.get('/layout/')

    def getuser(self):
        return self.app.get('/user/')

    def test_reg_login_layout(self):
        assert self.register("hello","world").status_code == 200
        assert  '登录成功' in str(self.login("hello","world").data,encoding='utf-8')
        assert  'hello' in str(self.app.get('/user/').data,encoding='utf-8')
        assert   '登出成功' in  str(self.logout().data,encoding='utf-8')
        assert  '重新' in str(self.app.get('/user/').data,encoding='utf-8')
        assert  "密码错误" in   str(self.login("hello","wor").data,encoding='utf-8')


