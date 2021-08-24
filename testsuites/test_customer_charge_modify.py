# -*- coding: utf-8 -*-
import time
import unittest
from framework.browser_engine import BrowserEngine
from pageobjects.customer_page import FirstPage
from pageobjects.c_chargemodify_page import ChargePage
# from pageobjects.login_page import LoginPage
from testsuites.test_login import LoginAction
from framework.logger import Logger


# create a logger instance
logger = Logger(logger="ChargeModifyPage").getlog()


class Charge_Modify(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        browse = BrowserEngine(cls)
        cls.driver = browse.open_browser(cls)
        # 登录系统
        LoginAction.login(cls, "bessie", "Zhang12345!")
        # 打开客户列表
        firstpage = FirstPage(cls.driver)
        # firstpage.click_swbtn()
        firstpage.click_cmbtn()
        firstpage.click_clbtn()
        # 切换到客户列表框架
        firstpage.switch_iframe1()

    # @classmethod
    # def tearDownClass(cls):
    #     cls.driver.quit()

    # 转交客户销售
    def test_customer_transsale(self):
        # # 打开客户列表
        # firstpage = FirstPage(self.driver)
        # # firstpage.click_swbtn()
        # firstpage.click_cmbtn()
        # firstpage.click_clbtn()
        # # 切换到客户列表框架
        # firstpage.switch_iframe1()
        chargepage = ChargePage(self.driver)
        chargepage.search_testdata("bessie")
        chargepage.check_firstdata()
        chargepage.get_saleinfo()
        chargepage.click_chargebtn()
        chargepage.charge_saleselect("admin")
        chargepage.get_t_alert(u"保存成功")

    # 添加协作人
    @unittest.skip('')
    def test_customer_transassist(self):
        self.driver.refresh()
        chargepage = ChargePage(self.driver)
        chargepage.search_atestdata("bessie")
        chargepage.check_firstdata()
        chargepage.get_assistinfo()
        chargepage.click_chargebtn()
        chargepage.charge_assistselect("admin")
        chargepage.get_t_alert(u"保存成功")
        logger.info(u"======转交客户销售成功======")


if __name__ == '__main__':
    unittest.main()
