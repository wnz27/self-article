# -*- coding:utf-8 -*-
# @UpdateTime : 2020/4/20 12:14 下午
# @description: 测试固件分离文件
import sys
from selenium import webdriver
import unittest
from abc import abstractmethod
from pageObject.config.driver_config import IMPLICIT_TIME, CHROME_OPTIONS


class BaseTestUnit(unittest.TestCase):
    # 类初始化
    # 设置测试依赖的驱动默认测试都跑chrome浏览器，需要老师们指定使用chrome
    driver = webdriver.Chrome(chrome_options=CHROME_OPTIONS)  # 后台跑自动化时使用
    # driver = webdriver.Chrome()  # 开发用，看清操作
    page_obj = None  # 具体页面对象

    @classmethod
    def setUpClass(cls):
        """
        对driver做一些可能的初始化。
        IMPLICIT_TIME，传入驱动的implicitly_wait方法里:
        隐式等待的时间，单位为秒，这个值会被驱动的implicitly_wait方法使用，
        当使用了隐士等待执行测试的时候，如果 WebDriver没有在DOM中找到元素，将继续等待，超出设定时间后则抛出找不到元素的异常
        换句话说，当查找元素或元素并没有立即出现的时候，隐式等待将等待一段时间再查找DOM，默认的时间是0
        一旦设置了隐式等待，则它存在整个 WebDriver 对象实例的声明周期中，隐式的等到会让一个正常响应的应用的测试变慢，
        它将会在寻找每个元素的时候都进行等待，这样会增加整个测试执行的时间。
        """
        cls.driver.implicitly_wait(IMPLICIT_TIME)  # 设置查找元素的隐式等待时间

    @classmethod
    def tearDownClass(cls):
        """
        关闭驱动
        """
        cls.driver.quit()

    @abstractmethod
    def setUp(self):
        """
        增加abstractmethod装饰器强制子类实现这个方法
        获取数据的逻辑可以在这里添加或者根据情况写进每个测试对应的方法
        如果测试量小还好，随着项目增大，测试数据累计，如果都写在setup里面
        会不会出现极大消耗cpu和内存的情况，对此可能未来优化的方式是构建数据生成器。
        在这里初始化page_obj和handle_data_obj，并对具体URL做更新
        TODO 构建测试数据生成器，提升测试数据性能，一个方向是对测试数据的handler做迭代
        """
        pass
