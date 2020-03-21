# -*- coding: utf-8 -*-
"""
使用函数完成用户登录和注册功能
#先让用户选择，是登陆还是注册
#选择序号完毕之后，运行相应的程序，
#验证成功之后，可以让其继续选择，登陆还是注册，还可以选择退出
"""
#方法一：有参装饰器
def user_auth(user_role):  # 'SVIP'
    def wrapper(func):
        def inner(*args, **kwargs):
            if user_role == 'SVIP':
                # 添加超级用户的功能
                res = func(*args, **kwargs)
                return res
            elif user_role == '普通用户':
                print('普通用户')
                # 添加普通用户的功能
                res = func(*args, **kwargs)
                return res

        return inner
    return wrapper

@user_auth('普通用户')            #在这里wrapper=user_auth('普通用户')
def index(): 
    print('普通用户')
    pass 
index()

#方法二：无参装饰器
def user_auth(user_role):  # 'SVIP'
    def wrapper(func):
        def inner(*args, **kwargs):
            if user_role == 'SVIP':
                # 添加超级用户的功能
                res = func(*args, **kwargs)
                return res
            elif user_role == '普通用户':
                print('普通用户')
                # 添加普通用户的功能
                res = func(*args, **kwargs)
                return res

        return inner
    return wrapper
wrapper = user_auth('普通用户')
@wrapper          #<--- 返回结果(wrapper) <---- user_auth()
def index():
    print('普通用户')
    pass
index()


#加2个修饰器
def say_hi(func):
    def wrapper(*args, **kwargs):
        print("HI")
        ret = func(*args, **kwargs)
        print('人生苦短，我用pyhton.')
    return wrapper
def say_yo(func):
    def wrapper(*args, **kwargs):
        print("YO")
        return func(*args, **kwargs)
    return wrapper

@say_hi
@say_yo
def func():
	print("Tank & Jason")

func()
