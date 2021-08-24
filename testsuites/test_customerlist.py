# -*- coding: utf-8 -*-
import time
import unittest
from framework.browser_engine import BrowserEngine
from pageobjects.customer_page import FirstPage
# from pageobjects.login_page import LoginPage
from testsuites.test_login import LoginAction
import random
from framework.logger import Logger


# create a logger instance
logger = Logger(logger="CustomerPage").getlog()


class CustomerList(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        browse = BrowserEngine(cls)
        cls.driver = browse.open_browser(cls)
        # 登录系统
        LoginAction.login(cls, 'bessie', 'Zhang12345!')

    # @classmethod
    # def tearDownClass(cls):
    #     cls.driver.quit()

    # 新增客户基础测试用例
    # @unittest.skip('')
    def test_Add(self):
        # 打开客户列表
        firstpage = FirstPage(self.driver)
        # firstpage.click_swbtn()
        firstpage.click_cmbtn()
        firstpage.click_clbtn()
        # 切换到客户列表框架
        firstpage.switch_iframe1()
        # 点击新增客户按钮
        firstpage.click_addbtn()
        # 输入客户名称
        now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
        cname = u"测试客户" + now
        firstpage.cname_input(cname)
        firstpage.ccontact_input(u"bstest")
        # 输入客户手机(随机生成)
        firstpage.cphone_input(firstpage.RandomPhone())
        # 选择客户来源
        firstpage.csource_select(u"测试")
        # 选择客户销售
        # firstpage.csale_select(1)
        # 选择客户协作人
        firstpage.cassistant_select("admin")
        # 选择客户所属国家
        firstpage.ccountry_select(u"中国")
        # 选择客户所属省市区
        firstpage.cprovince_select(u"河北省")
        # firstpage.ccity_select(u"石家庄市")
        # firstpage.carea_select(u"长安区")
        # 输入详细地址
        firstpage.caddress_input(u"测试地址102号")
        # 选择行业
        # firstpage.cprofession_select(u"服装")
        # # 选择人员规模
        # firstpage.cscale_select(u"20-99人")
        # # 选择年销售额
        # firstpage.cannualsale_select(u"10-100万")
        # 填写邮箱（随机生成）
        em = ''.join(random.sample(["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"], 5))
        cemail = em + "@qq.com"
        firstpage.cemail_input(cemail)
        # 填写座机
        cp = ''.join(random.sample(["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"], 5))
        firstpage.cphonecall_input(cp)
        # 填写传真
        cf = ''.join(random.sample(["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"], 5))
        firstpage.cfax_input(cf)
        # 填写备注
        firstpage.cremark_input(u"这是一段测试备注内容。")
        # 点击保存
        firstpage.click_savebtn()
        # 获取客户名称，判断是否添加成功
        firstpage.get_cnamedata(cname)
        logger.info(u"======新增客户成功======")
        time.sleep(1)

    # 客户名称重复验证
    @unittest.skip('')
    def test_repeat_cname(self):
        firstpage = FirstPage(self.driver)
        first_cname = firstpage.get_firstdata()
        # 点击新增客户按钮
        firstpage.click_addbtn()
        # 输入客户名称
        firstpage.cname_input(first_cname)
        # 输入客户手机(随机生成)
        firstpage.cphone_input(firstpage.RandomPhone())
        # 选择客户来源
        firstpage.csource_select_t(u"测试")
        # 点击保存
        firstpage.click_savebtn()
        # 获取客户名称，判断客户是否重复并提示
        firstpage.get_c_alert(u"客户名称重复")
        logger.info(u"======客户名称重复验证成功======")
        firstpage.click_cancelbtn()
        time.sleep(1)

    # 手机号重复验证
    @unittest.skip('')
    def test_repeat_cphone(self):
        firstpage = FirstPage(self.driver)
        # # firstpage.click_swbtn()
        # firstpage.click_cmbtn()
        # firstpage.click_clbtn()
        # # 切换到客户列表框架
        # firstpage.switch_iframe1()
        first_cphone = firstpage.get_firstdata_phone()
        firstpage.close_cinfo()
        firstpage.click_addbtn()
        now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
        cname = u"测试客户" + now
        firstpage.cname_input(cname)
        firstpage.cphone_input(first_cphone)
        # 选择客户来源
        firstpage.csource_select_t(u"测试")
        # 点击保存
        firstpage.click_savebtn()
        firstpage.get_c_alert(u"客户手机重复")
        logger.info(u"======客户手机重复验证成功======")
        firstpage.click_cancelbtn()


if __name__ == '__main__':
    unittest.main()

