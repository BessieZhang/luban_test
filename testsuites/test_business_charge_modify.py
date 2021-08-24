# -*- coding: utf-8 -*-
import time
import unittest
from framework.browser_engine import BrowserEngine
from pageobjects.customer_page import FirstPage
from pageobjects.business_page import BusinessPage
from pageobjects.b_chargemodify_page import BChargePage
# from pageobjects.login_page import LoginPage
from testsuites.test_login import LoginAction
from framework.logger import Logger


# create a logger instance
logger = Logger(logger="BChargeModifyPage").getlog()


class BCharge_Modify(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        browse = BrowserEngine(cls)
        cls.driver = browse.open_browser(cls)
        # 登录系统
        LoginAction.login(cls, "bessie", "Zhang12345!")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    # 转交商机负责人
    def test_business_transcharge(self):
        # 打开商机列表
        firstpage = FirstPage(self.driver)
        firstpage.click_swbtn()
        firstpage.click_cmbtn()
        buinesspage = BusinessPage(self.driver)
        buinesspage.click_blbtn()
        # 切换到商机列表框架
        buinesspage.switch_iframe2()
        bchargepage = BChargePage(self.driver)
        bchargepage.search_testdata("bessie")
        bchargepage.check_firstdata()
        bchargepage.click_bchargebtn()
        bchargepage.bcharge_select("admin")
        bchargepage.get_tb_alert(u"转交成功")
        logger.info(u"======转交商机负责人成功======")


if __name__ == "__main__":
    unittest.main()