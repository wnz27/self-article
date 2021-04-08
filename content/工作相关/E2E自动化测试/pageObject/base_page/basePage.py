# -*- coding:utf-8 -*-
# @UpdateTime : 2020/4/17 3:00 下午
from __future__ import print_function

from selenium.webdriver.support.wait import WebDriverWait  # 显示等待
from selenium.webdriver.support import expected_conditions as EC  # 判断元素是否被定位到


class BasePage(object):  # 所有页面的基础类
    def __init__(self, url, driver=None):  # 定义驱动和地址
        self.url = url
        self.driver = driver

    def find_element(self, *el_use_by_location):  # 封装元素定位方式
        """
        el_use_by_location: 元素定位，元组，使用的是By类来查找，el_use_by_location的形式：(By.ID, 'mobilePhone')
        """
        if self.driver is None:
            raise NoneDriverException(u"驱动未找到，请在测试类setUp方法中，初始化页面时传入测试基类附带的驱动")
        else:
            try:
                WebDriverWait(self.driver, 5).until(
                    EC.visibility_of_element_located(el_use_by_location))  # 这个位置的元素是否有宽和高，具体可以看下方法描述，讲的很清晰
                return self.driver.find_element(*el_use_by_location)
            except Exception as errorMessage:
                print(u"元素定位在页面中无法找x到！" + " exception: " + errorMessage)


class NoneDriverException(Exception):
    def __init__(self, error_msg):
        super(NoneDriverException, self).__init__()
        print(error_msg)
