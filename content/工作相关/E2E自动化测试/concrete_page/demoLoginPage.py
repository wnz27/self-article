# -*- coding:utf-8 -*-
# @UpdateTime : 2020/4/20 11:13 上午
from pageObject.base_page.basePage import BasePage  # 导入BasePage基础类
from selenium.webdriver.common.by import By  # 定位方式,用By定位
from time import sleep


class LoginPage(BasePage):
    # 定位属性定义，如果页面变化可能只需要修改这里的属性，把小流程封装在方法里    <--------  属性说明

    # 用户名定位
    username_loc = (By.ID, 'mobilePhone')
    # 密码定位
    password_loc = (By.ID, 'password')
    # "登录"按钮
    loginBtn_loc = (By.ID, 'LoginBtn')
    # 退出连接
    logoutBtn_loc = (By.CSS_SELECTOR, 'a.fc-blue.mr-5')
    # 用户名为空定位
    userNull_loc = (By.CSS_SELECTOR, '# error > span')
    # 密码为空定位
    passWordNull_loc = (By.CSS_SELECTOR, '# ERROR > span')

    # 页面级别的行为定位，粒度从细到粗。                 <--------  方法说明

    # 打开登录页面
    def open_login_page(self):
        self.driver.get(self.url)
        self.driver.refresh()
        self.driver.maximize_window()
        sleep(0.5)

    # 输入用户名
    def input_user_name(self, username):
        self.find_element(*self.username_loc).sendkeys(username)

    # 输入密码
    def input_password(self, password):
        self.find_element(*self.password_loc).sendkeys(password)

    # 单击"登录"按钮
    def click_login_btn(self):
        self.find_element(*self.loginBtn_loc).click()

    # 获取登录完成的信息
    @property
    def get_login_text(self):
        return self.find_element(*self.loginBtn_loc).text

    # 获取登出的信息
    @property
    def get_logout_text(self):
        return self.find_element(*self.logoutBtn_loc).text

    # 用户名为空的提示信息
    @property
    def get_user_null_text(self):
        return self.find_element(*self.userNull_loc).text

    # 密码为空的提示信息
    @property
    def get_password_null_text(self):
        return self.find_element(*self.passWordNull_loc).text

    # 组装成登录流程
    def login_page_login_pro(self, username, password):
        self.input_user_name(username)
        self.input_password(password)
        self.click_login_btn()
