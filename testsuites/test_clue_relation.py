# -*- coding: utf-8 -*-
import time
import unittest
from framework.browser_engine import BrowserEngine
from pageobjects.clue_page import CluePage
# from pageobjects.login_page import LoginPage
from testsuites.test_login import LoginAction
import random
from framework.logger import Logger


# create a logger instance
logger = Logger(logger="CluePage").getlog()


class ClueList(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        browse = BrowserEngine(cls)
        cls.driver = browse.open_browser(cls)
        # 登录系统
        LoginAction.login(cls, 'bessie', 'Zhang12345!')

    # @classmethod
    # def tearDownClass(cls):
    #     cls.driver.quit()

    # 线索关联商机__关联已有客户测试用例
    # @unittest.skip('')
    def test_Relation(self):
        # 打开线索列表
        cluepage = CluePage(self.driver)
        cluepage.click_cmbtn()
        cluepage.click_clbtn()
        # 切换到线索列表框架
        cluepage.switch_iframe1()
        cluepage.search_clue("XS2020090738092877")
        cluepage.click_searchbtn()
        cluepage.click_resultid()
        cluepage.click_relationtab()
        cluepage.click_relateexistingcustomer()
        cluepage.click_cluetransfer_btn()
        cluepage.search_existing_customer("qa-1598609519499")
        cluepage.click_surebtn()
        cluepage.check_customer()
        cluepage.click_customer_next()
        cluepage.click_existing_contact()
        cluepage.check_contact()
        cluepage.click_contact_next()
        cluepage.choose_business_title(2)
        cluepage.choose_dealdate()
        cluepage.bcharge_select(2)
        # cluepage.bassistant_select(2, 3)
        cluepage.bsource_select(u"平台订购")
        cluepage.bremark_input(u"备注")
        cluepage.bproduct_add()


if __name__ == '__main__':
    unittest.main()
