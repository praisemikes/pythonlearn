#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
迭代器

"""


# l2 = [1, 2, 3, 4, 5, 6, 7, 8]
# l2_obj = l2.__iter__()  #1.将可迭代对象转化成迭代器
# print(12_obj)   #invalid decimal literal变量名不能由数字开头

list2 = [1, 2, 3, 4, 5, 6, 7, 8]
obj = list2.__iter__()  #1.将可迭代对象转化成迭代器
print(obj)   #结果是内存地址

# while True:
    # try:
        # i = obj.__next__() #内部使用__next__方法取值
        # print(i)
    # except Exception: #运用了异常处理去处理报错
        # break
		

#第二个厂商，先生产出50套，给老板看

# def func1():
    # for i in range(1,10001):
        # yield 'ARMAIN服装%d套' % i
# g = func1()
# for i in range(1,51):
    # print(g.__next__())
'''执行输出：
...
ARMAIN服装48套
ARMAIN服装49套
ARMAIN服装50套
'''
#一个厂商可以生产出10000套 
#最终老板只要200套，先订50套，再150套

# def func1():
    # for i in range(1,10001):
        # yield 'ARMAIN服装%d套' % i
# g = func1()

# for i in range(1,51):
    # print(g.__next__())
# #再执行150次，注意，它是从51开始的
# print('*'*30)
# for j in range(150):
    # print(g.__next__())
	
'''执行输出：

ARMAIN服装51套
ARMAIN服装52套
ARMAIN服装53套
..
ARMAIN服装200套
'''
#对于列表而言，for循环是从开始
#对于生成器而言，它是有指针的，__next__一次，指针向前一次。
#它不能从头开始，必须依次执行才行。

#如何写一个生成器
# def fun1():
    # yield 1
    # #print(yield)  #语法错误
    # yield
# fun1()      #没有输出
# print(fun1().__next__())
#输出1

#send方法
def generator():
    print(123)
    content = yield 1
    print('=======',content)
    print(456)
    yield

g = generator()
# ret = g.__next__()
# print('***',ret)    #123，  ====1

ret = g.__next__()
print('***',ret)
print('*'*50)
ret = g.send('hello')   #send的前面要有next__(),
print('***',ret)

'''
执行输出：
123
*** 1
************
======= hello
456
*** None

#send 获取下一个值的效果和next基本一致
只是在获取下一个值的时候，给上一yield的位置传递一个数据
使用send的注意事项
　　 第一次使用生成器的时候 是用next获取下一个值
 　　最后一个yield不能接受外部的值
'''