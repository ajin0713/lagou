# -*- coding: utf-8 -*-
# @Time   :2021/2/26 6:05 下午
# @Author :zhulihua
# @File   :conftest.py
import pytest
from Hogwards.python_code.calc import Calculator

@pytest.fixture(scope='module')
def get_calc():
    print('获取计算器实例')
    calc = Calculator()
    return calc
