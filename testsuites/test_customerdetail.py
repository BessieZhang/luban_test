# -*- coding: utf-8 -*-
import time
import unittest
from framework.browser_engine import BrowserEngine
from pageobjects.customer_page import FirstPage
from pageobjects.customerdetail_page import CustomerDetailPage
from testsuites.test_login import LoginAction
import random
from framework.logger import Logger


# create a logger instance
logger = Logger(logger="CustomerDetailPage").getlog()


class CustomerDetail(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        browse = BrowserEngine(cls)
        cls.driver = browse.open_browser(cls)
        # 登录系统
        LoginAction.login(cls, 'bessie', 'Zhang12345!')
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

    # 打标签
    @unittest.skip('')
    def test_addtag(self):
        # # 打开客户列表
        # firstpage = FirstPage(self.driver)
        # # firstpage.click_swbtn()
        # firstpage.click_cmbtn()
        # firstpage.click_clbtn()
        # # 切换到客户列表框架
        # firstpage.switch_iframe1()
        customerdetailpage = CustomerDetailPage(self.driver)
        customerdetailpage.target_customer(u"测试客户2020-01-04-14_56_19")
        customerdetailpage.click_addtag_btn()
        customerdetailpage.check_target_tagname(u"测试账号")
        customerdetailpage.click_savetag_btn()
        customerdetailpage.get_alert(u"保存成功")
        customerdetailpage.close_detailpage()

    # 新增联系人
    @unittest.skip('')
    def test_addcontact(self):
        customerdetailpage = CustomerDetailPage(self.driver)
        customerdetailpage.target_customer(u"测试客户2020-01-04-14_56_19")
        customerdetailpage.switchto_contact_tab()
        customerdetailpage.click_contactbtn()
        customerdetailpage.cc_name_input(u"联系人1")
        customerdetailpage.cc_phone_input(customerdetailpage.RandomPhone())
        customerdetailpage.cc_post_input(u"仓管")
        customerdetailpage.cc_save_btn()
        customerdetailpage.get_alert(u"添加成功")


if __name__ == '__main__':
    unittest.main()

