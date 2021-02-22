# -*- coding: utf-8 -*-
# @Time   :2021-02-02 16:36
# @Author :zhulihua
# @File   :money.py
'''
原有存款 1000 元，发工资之后存款变为 2000 元
定义模块
1，money.py saved_money = 1000
2,定义发工资模块send_money，用来增加收入计算
3,定义工资查询模块select_money，用来展示工资金额
4,定义一个start.py，启动文件展示最终存款金额
'''

saved_money = 1000


def send_money():
    global  saved_money
    saved_money +=  1000
    print('发工资了')

def select_money():
    print(f'现在有存款{saved_money}')

if __name__ == '__main__':
    send_money()
    select_money()
