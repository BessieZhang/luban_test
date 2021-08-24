# -*- coding: utf-8 -*-
import time
import unittest
from framework.browser_engine import BrowserEngine
from pageobjects.customer_page import FirstPage
from pageobjects.business_page import BusinessPage
# from pageobjects.login_page import LoginPage
from testsuites.test_login import LoginAction
from framework.logger import Logger


# create a logger instance
logger = Logger(logger="BusinessPage").getlog()


class BuinessList(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        browse = BrowserEngine(cls)
        cls.driver = browse.open_browser(cls)
        # 登录系统
        LoginAction.login(cls, 'bessie', 'Zhang12345!')

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    # @unittest.skip("")
    # 新增商机测试用例
    def test_Addbusiness1(self):
        # 打开商机列表
        firstpage = FirstPage(self.driver)
        firstpage.click_swbtn()
        firstpage.click_cmbtn()
        buinesspage = BusinessPage(self.driver)
        buinesspage.click_blbtn()
        # 切换到商机列表框架
        buinesspage.switch_iframe2()
        # 点击新增商机按钮
        buinesspage.click_addbtn()
        # 输入商机标题
        now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
        bname = u"测试商机" + now
        buinesspage.btitle_input(bname)
        # 选择所属客户
        buinesspage.bcustomer_check(u"贝茜测试")
        time.sleep(1)
        # 选择联系人
        buinesspage.bcntperson_select(1)
        # 填写预计成交日期
        buinesspage.bdealdate_input("2020-03-03")
        time.sleep(1)
        # 选择负责人
        # 选择协作人
        buinesspage.bassistant_select(2, 41)
        # 选择来源
        buinesspage.bsource_select(7)
        # 填写备注
        buinesspage.bnote_input(u"这是一个测试商机。")
        # 选择商品
        buinesspage.bproduct_select(u"专业版")
        # 保存商机
        buinesspage.click_savebtn()
        # 获取提示信息
        buinesspage.get_b_alert(u"新增商机成功！")
        # 写跟进--取消
        buinesspage.click_cancelbtn()
        logger.info(u"======新增商机成功======")


if __name__ == '__main__':
    unittest.main()