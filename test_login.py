from python_class8.db import DB
import time
# 创建连接
db = DB(host='localhost', port=3306, user='root', password='root',database='stu',dict=True)
# 创建表格
sql = """
    create table if not exists users(
        username varchar (12) not null,
        password varchar (20) not null ,
        primary key(username)
    )engine=InnoDB default charset=utf8
"""
db.common(sql)

while True:
    print("-------------------请输入所需要的具体操作,1:登录,2:注册--------------------")
    num = input("请输入具体的操作编码:")
    if num.isdigit():
        num = int(num)
        if num == 1:
            username = input("请输入用户名:")
            password = input("请输入密码:")
            sql = 'select password from users where username=%s'
            # 执行查询操作
            result = db.select(sql, username)
            if len(result) == 0:
                print("该用户名尚未注册,请前往注册")
            else:
                if result[0].get('password') == password:
                    print("登录成功!")
                    num = input("请选择对应的操作,1:修改密码,2:注销用户")
                    if num.isdigit():
                        num = int(num)
                        if num == 1:
                            username = input("请重新输入用户名:")
                            password = input("请输入新密码:")
                            sql = 'update users set password=%s where username = %s'
                            result = db.update(sql, [password, username])
                            if result > 0:
                                print("密码修改成功!请尝试重新登录")
                            else:
                                print("密码修改失败!")
                        elif num == 2:
                            username = input("该操作将彻底删除你的账户,无法找回,请仔细考虑,输入用户名确定注销:")
                            # time.sleep(0.5)
                            t = 0.5
                            for i in range(5):
                                print(">")
                                t = 0.5-0.1
                                time.sleep(t)
                            sql = 'delete from users where username=%s'
                            result = db.delete(sql, username)
                            if result > 0:
                                print("已注销!谢谢使用")
                            else:
                                print("失败,请重新尝试!")
                    else:
                        print("输入编码错误,请检查后重新输入!")
                else:
                    print("密码输入错误!")
        elif num == 2:
            username = input("请输入用户名:")
            password = input("请输入密码:")
            sql = 'select count(username) from users where username=%s'
            result = db.select(sql, username)
            if result[0]['count(username)'] == 0:
                sql = 'insert into users(username, password) values (%s, %s)'
                result = db.insert(sql, [(username, password)])
                if result > 0:
                    print("注册成功!")
                else:
                    print("注册失败,请重新注册!")
            else:
                print("对不起,该用户名已经注册")
        else:
            print("输入编码错误,请检查后重新输入!")
    else:
        print("输入编码错误,请检查后重新输入!")
