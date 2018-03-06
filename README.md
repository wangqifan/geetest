# geetest
作业



安装
------------
如果你是linux用户 For Linux 

  
   pip install -r requirements.txt

如果你是 Windows用户, 
    pass

运行
-------
  * 运行管理脚本
  ```
      python manage.py
   ```
   * 运行服务
       ```
      python server.py
      ```
      
    * 运行测试
      ```
      python test.py
      `
      
API 文档
-------
  * 注册用户
   get和post都可以，以get为例 http://account.geetest.com/reg/?username='hello'&password='world'  <br>
   返回json例如
   
   ```
     {
         "message": "注册成功", 
          "success": true
     }
   ```
   * 登录
     get和post都可以，以get为例 http://account.geetest.com/reg/?username='hello'&password='world'  <br>
     返回json，例如
     ```
      {
           "message": "登录成功", 
           "success": true
      }
      ```
      * 登出
      get访问http://account.geetest.com/layout/
      ```
         {
           "message": "登出成功", 
            "success": true
         }
      ```
     
   
   
