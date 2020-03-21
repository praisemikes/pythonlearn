# -*- coding: utf-8 -*-
"""
使用函数完成用户登录和注册功能
#先让用户选择，是登陆还是注册
#选择序号完毕之后，运行相应的程序，
#验证成功之后，可以让其继续选择，登陆还是注册，还可以选择退出
"""

import time,os
 
#文件名
file_name = 'user_list.txt'
  
def file_exists(*args,**kwargs):
    '''
    # 判断用户列表文件是否存在
    :return: True 存在 False 不存在
    '''
    # 判断文件是否存在
    if os.path.exists(file_name):
        return True
    else:
        with open(file_name, encoding='utf-8', mode='w') as mk:
            mk.write('张三    123')
            return False
 
 
def registered_username(username):
    '''
    #判断注册用户名是否可用
    :param username: 用户名
    :return: True 可用(用户不存在) False 不可用(用户已存在)
    '''
    # 纯用户名列表，不包含密码
    user_list = []
    with open(file_name, encoding='utf-8') as f1:
        for i in f1:
            # 去空格,以空格切割,txt文件转换为列表
            li = i.strip().split()    # [张三，123]
            #print(li)        # [张三，123]
            # 将用户名追加到列表中
            user_list.append(li[0])
        #print(user_list)     #['张三','haung','huang'],只增加li[0]
        # 判断用户名是否存在列表中
        if username in user_list:
            # 返回False
            return False
        else:
            return True
 
 
def write_file(username,password):
    '''
    #写入用户列表文件
    :param username: 用户名
    :param password: 密码
    :return: True 写入成功 False 写入失败
    '''
    with open(file_name, encoding='utf-8', mode='a') as f2:
        f2.write('\n{}    {}'.format(username, password))
        return True
 
 
def username_password(username,password):
    '''
    #判断用户名和密码是否匹配
    :param username: 用户名
    :param password: 密码
    :return: True 匹配成功 False 匹配失败
    '''
    # print(username,password)
    with open(file_name, encoding='utf-8', mode='r') as f3:
        for i in f3:
            # print(i)
            # 去空格,以空格切割,转换为列表
            li = i.strip().split()  # [张三，123]
            # 判断用户名和密码是否匹配
            if username == li[0] and password == li[1]:
                result = True
                # 当找到匹配时,跳出循环
                break
            else:
                result = False
        # 当整个用户列表遍历完成之后，再return
        return result
 
 
def register(*args,**kwargs):
    '''
    注册逻辑
    :return:
    '''
    while True:
        username = input('请输入注册的用户名,或输入q返回菜单：').strip()
        if username == '':
            print('用户名为空,请重新输入!')
        elif username.upper() == 'Q':
            break
        else:
            # 执行判断用户名函数
            result = registered_username(username)
            if result:
                password = input('请输入您的注册的密码：').strip()
                # 判断密码
                if password == '':
                    print('密码为空,请重新输入!')
                else:
                    # 执行写入用户列表文件函数
                    result = write_file(username, password)
                    if result:
                        print('注册成功!，您的用户名为: {}\n倒计时2秒返回菜单!'.format(username))
                        time.sleep(2)
                        user_menu()
                    else:
                        print('注册失败!请重试')
            else:
                print('用户名已经存在,请重新输入!')
 
 
def login(count=0,max=3):
    '''
    登录逻辑
    :param count: 初始失败次数
    :param max: 最大失败次数
    :return:
    '''
    while count < max:
        count += 1
        username = input('请输入用户名：').strip()
        password = input('请输入密码：').strip()
        # 执行验证用户名和密码函数
        result = username_password(username,password)
        if result:
            print('登陆成功\n倒计时1秒返回菜单!')
            time.sleep(1)
            user_menu()
            break
        else:
            print('用户名或密码错误,还剩余{}次机会!'.format(max - count))
 
    # 返回主菜单
    user_menu()
 
 
def user_menu(*args,**kwargs):
    '''
    # 用户菜单
    '''
    # 判断文件是否存在，不存在创建文件
    file_exists()
    # 循环
    while True:
        # 打印菜单
        menu = ['注册', '登录', '退出']
        print('bbs系统'.center(25, '#'))
        for i in range(len(menu)):
            print('{}\t{}'.format(i + 1, menu[i]))
        print(''.center(27, '#'))
        number = input('请选择序号: ').strip()
        if number == '1':
            # 执行注册程序
            register()
        elif number == '2':
            # 执行登录程序
            login()
        elif number == '3':
            exit()
        else:
            print('输入错误,请重新输入!')
 

if __name__ == '__main__': 
# 执行菜单
    user_menu()