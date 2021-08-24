# -*- coding: utf-8 -*-
import time
import unittest
from framework.browser_engine import BrowserEngine
from pageobjects.login_page import LoginPage


class LoginAction(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        browse = BrowserEngine(cls)
        cls.driver = browse.open_browser(cls)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    @staticmethod
    def login(self, username, password):
        loginpage = LoginPage(self.driver)
        loginpage.click_user_tab()
        loginpage.type_username(username)
        loginpage.type_passwd(password)
        loginpage.click_sub()
        time.sleep(2)
        loginpage.get_windows_img()


if __name__ == '__main__':
    unittest.main()
