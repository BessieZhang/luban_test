# -*- coding: utf-8 -*-
from framework.base_page import BasePage


class LoginPage(BasePage):
    # 账号登录tab
    user_tab = "tab-account"
    # 用户名输入框
    username_input = "xpath=>//*[@id='pane-account']/div/form/div[1]/div/div/div/div/input"
    # 密码输入框
    passwd_input = "xpath=>//*[@id='pane-account']/div/form/div[2]/div/div/div/div/input"
    # 登录按钮
    submit_bt = "xpath=>//*[@id='pane-account']/div/form/div[4]/div/button"

    # 切换到账号登录
    def click_user_tab(self):
        self.driver.find_element_by_id("tab-account").click()
        self.sleep(1)

    # 输入用户名
    def type_username(self, text):
        self.type(self.username_input, text)

    # 输入密码
    def type_passwd(self, text):
        self.type(self.passwd_input, text)

    # 点击登录按钮
    def click_sub(self):
        self.click(self.submit_bt)
        self.sleep(2)