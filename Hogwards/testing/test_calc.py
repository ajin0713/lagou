# -*- coding: utf-8 -*-
# @Time   :2021/2/26 6:06 下午
# @Author :zhulihua
# @File   :test_calc.py
import allure
import pytest
import yaml

# 从conftest.py中获取实例
with open('./datas/calc.yaml') as f:
    datas = yaml.safe_load(f)
    # 取加法参数化的值
    add_datas = datas['add']['datas']

    # 取除法参数化的值
    div_datas = datas['div']['datas']

    # 取减法参数化的值
    sub_datas = datas['sub']['datas']
    # 为测试用例命名
    sub_myid = datas['sub']['myid']

    # 取乘法参数化的值
    mul_datas = datas['mul']['datas']

#fixture带参数传递，通过 get_add_datas 方法获取加法的参数
@pytest.fixture(params=add_datas)
def get_add_datas(request):
    print('开始计算')
    data = request.param
    print(f'测试数据为：{data}')
    yield data
    print('结束计算')

#fixture带参数传递，通过 get_add_datas 方法获取除法的参数
@pytest.fixture(params=div_datas)
def get_div_datas(request):
    print('开始计算')
    data = request.param
    print(f'测试数据为：{data}')
    yield data
    print('结束计算')

#fixture带参数传递，通过 get_add_datas 方法获取减法的参数
@pytest.fixture(params=sub_datas,ids=sub_myid)
def get_sub_datas(request):
    print('开始计算')
    data = request.param
    print(f'测试数据为：{data}')
    yield data
    print('结束计算')

#fixture带参数传递，通过 get_add_datas 方法获取乘法的参数
@pytest.fixture(params=mul_datas)
def get_mul_datas(request):
    print('开始计算')
    data = request.param
    print(f'测试数据为：{data}')
    yield data
    print('结束计算')

@allure.feature('测试计算器')
class TestCalc:

    # 测试用例的执行顺序
    @pytest.mark.run(order=1)
    @allure.story('测试加法')
    def test_add(self,get_calc,get_add_datas):
        with allure.step('计算两个数相加的和'):
            result = get_calc.add(get_add_datas[0],get_add_datas[1])
        # 判断result 是浮点数，作出保留2位小数的处理
        if isinstance(result,float):
            result = round(result,2)
        # 得到结果之后，需要写断言
        assert result == get_add_datas[2]

    # 测试用例的执行顺序
    @pytest.mark.run(order=4)
    @allure.story('测试除法')
    def test_div(self,get_calc,get_div_datas):
        with allure.step('计算两个数相除'):
            result = get_calc.div(get_div_datas[0],get_div_datas[1])
        # 判断result 是浮点数，作出保留2位小数的处理
        if isinstance(result,float):
            result = round(result,2)
        # 得到结果之后，需要写断言
        assert result == get_div_datas[2]

    # 测试用例的执行顺序
    @pytest.mark.run(order=2)
    @allure.story('测试减法')
    def test_sub(self,get_calc,get_div_datas):
        with allure.step('计算两个数相减的差'):
            result = get_calc.sub(get_sub_datas[0],get_sub_datas[1])
        # 判断result 是浮点数，作出保留2位小数的处理
        if isinstance(result,float):
            result = round(result,2)
        # 得到结果之后，需要写断言
        assert result == get_sub_datas[2]

    # 测试用例的执行顺序
    @pytest.mark.run(order=3)
    @allure.story('测试乘法')
    def test_mul(self,get_calc,get_mul_datas):
        with allure.step('计算两个数相除'):
            result = get_calc.div(get_mul_datas[0],get_mul_datas[1])
        # 判断result 是浮点数，作出保留2位小数的处理
        if isinstance(result,float):
            result = round(result,2)
        # 得到结果之后，需要写断言
        assert result == get_mul_datas[2]