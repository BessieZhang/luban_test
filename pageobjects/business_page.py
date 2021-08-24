# -*- coding:utf-8 -*-
from framework.base_page import BasePage


class BusinessPage(BasePage):
    # 商机列表菜单
    business_list = "xpath=>//*[@id='menuBar']/li[2]/ul/li[1]/ul/li[2]"
    # iframe
    iframe1 = "xpath=>//*[@id='tabsetMain']/contents/content[4]/c-iframe/iframe"
    # 新增商机按钮
    add_business = "xpath=>//*[@id='business-container']/div[2]/section/div/div/div/div[1]/div/button[1]"
    # 商机标题文本框
    b_title = "xpath=>//*[@id='business-container']/div[2]/div[2]/div/div/form/div[1]/div[1]/div/div/div/input"
    # 客户文本框
    b_customer = "xpath=>//*[@id='business-container']/div[2]/div[2]/div/div/form/div[1]/div[2]/div/div/div/input"
    # 选择客户搜索框
    b_customer_search = "xpath=>//*[@id='business-container']/div[2]/div[2]/div[2]/div/div[1]/div/div/div/input"
    # 选择客户查询按钮
    b_customer_searchbtn = "xpath=>//*[@id='business-container']/div[2]/div[2]/div[2]/div/div[1]/div/div/button"
    # 客户勾选框
    b_customer_checkbox = "xpath=>//*[@id='business-container']/div[2]/div[2]/div[2]/div/div[3]/div/div[3]" \
                          "/table/tbody/tr/td[2]/div/label"
    # 选择客户确认按钮
    b_customer_checkbtn = "xpath=>//*[@id='business-container']/div[2]/div[2]/div[2]/div/footer/div/button[1]"
    # 联系人下拉框
    b_cntperson = "xpath=>//*[@id='business-container']/div[2]/div[2]/div/div/form/div[2]/div[1]/div/div/div/div/span"
    # 联系人下拉数据列表
    bcntperson_options = "xpath=>/html/body/div[2]/div[1]/div[1]/ul/li/span"
    # 预计成交日期
    b_dealdate="xpath=>//*[@id='business-container']/div[2]/div[2]/div/div/form/div[2]/div[2]/div/div/div/input"

    # 负责人下拉框
    b_charge = "xpath=>//*[@id='business-container']/div[2]/div[2]/div/div/form/div[3]/div[1]/div/div/div/div[1]/span"
    # 负责人下拉数据列表
    bcharge_options = "xpath=>/html/body/div[3]/div[1]/div[1]/ul/li/span"

    # 协作人下拉框
    b_assistants = "xpath=>//*[@id='business-container']/div[2]/div[2]/div/div/form/div[3]/div[2]/div/div/div/div[2]/span"
    # 协作人下拉数据列表
    bassistants_options = "xpath=>/html/body/div[4]/div[1]/div[1]/ul/li/span"

    #来源label
    b_source_label= "xpath=>//*[@id='business-container']/div[2]/div[2]/div/div/form/div[4]/label"
    # 来源下拉框
    b_source = "xpath=>//*[@id='business-container']/div[2]/div[2]/div/div/form/div[4]/div/div/div[1]/span"
    # 来源下拉数据列表
    bsource_options = "xpath=>/html/body/div[5]/div[1]/div[1]/ul/li/span"
    # 备注输入框
    b_note = "xpath=>//*[@id='business-container']/div[2]/div[2]/div/div/form/div[5]/div/div/textarea"

    # +新增商品按钮
    b_addproduct = "xpath=>//*[@id='business-container']/div[2]/div[2]/div/div/div[1]/div[1]/button"
    # 选择商品按钮
    b_clickproduct = "xpath=>//*[@id='business-container']/div[2]/div[2]/div/div/div[1]/div[2]/div/div[3]/table/tbody/tr/td[3]/div/div/div/div/button"
    # 选择商品窗口--商品名称输入框
    b_searchproduct = "xpath=>//*[@id='business-container']/div[2]/div[2]/div/div/div[1]/div[3]/div/div/div[2]/div/div[1]/div[2]/div/input"
    # 选择商品窗口--搜索按钮
    b_searchbtn = "xpath=>//*[@id='business-container']/div[2]/div[2]/div/div/div[1]/div[3]/div/div/div[2]/div/div[1]/div[3]/button"
    # 选择商品窗口--第一条搜索结果
    b_result1 = "xpath=>//*[@id='business-container']/div[2]/div[2]/div/div/div[1]/div[3]/div/div/div[2]/div/div[2]/div[2]/div[3]/table/tbody/tr[1]"
    # 选择商品窗口--确定按钮
    b_resultbtn= "xpath=>//*[@id='business-container']/div[2]/div[2]/div/div/div[1]/div[3]/div/footer/div/button[1]"
    # 保存商机按钮
    b_savebtn = "xpath=>//*[@id='business-container']/div[2]/div[2]/div/div/div[2]/button[1]"

    # 写跟进取消按钮
    b_follow_cbtn = "xpath=>//*[@id='pane-first']/div[5]/button[2]"

    # 点击商机列表菜单
    def click_blbtn(self):
        try:
            self.click(self.business_list)
            self.sleep(2)
        except Exception as e:
            print e

    # 切换到商机列表iframe中
    def switch_iframe2(self):
        try:
            self.switch_iframe(1)
            self.sleep(2)
        except Exception as e:
            print e

    # 点击新增商机按钮
    def click_addbtn(self):
        try:
            self.click(self.add_business)
            self.sleep(2)
        except Exception as e:
            print e

    # 输入商机标题
    def btitle_input(self, text):
        try:
            self.type(self.b_title, text)
            self.sleep(2)
        except Exception as e:
            print e

    # 选择所属客户
    def bcustomer_check(self, text):
        try:
            self.click(self.b_customer)
            self.type(self.b_customer_search, text)
            self.click(self.b_customer_searchbtn)
            self.sleep(2)
            self.click(self.b_customer_checkbox)
            self.sleep(1)
            self.click(self.b_customer_checkbtn)
            # self.sleep(2)
        except Exception as e:
            print u"捕捉到异常信息: %s 。" % e

    # 选择联系人
    def bcntperson_select(self, index):
        try:
            self.click(self.b_cntperson)
            self.sleep(1)
            all_options = self.find_elements(self.bcntperson_options)
            obj_options = all_options[index]
            print obj_options
            obj_options.click()
        except Exception as e:
            print e

    # 填写预计成交日期
    def bdealdate_input(self, text):
        try:
            self.type(self.b_dealdate, text)
            self.find_element(self.b_source_label).click()
        except Exception as e:
            print e

    # # 选择负责人
    # def bcharge_select(self, index):
    #     try:
    #         self.click(self.b_charge)
    #         self.sleep(1)
    #         all_options = self.find_elements(self.bcharge_options)
    #         obj_options = all_options[index]
    #         print obj_options
    #         obj_options.click()
    #     except Exception as e:
    #         print e

    # # 选择协作人
    def bassistant_select(self, *args):
        try:
            self.click(self.b_assistants)
            self.sleep(1)
            all_options = self.find_elements(self.bassistants_options)
            print len(all_options)
            for a in args:
                all_options[a].click()
            self.sleep(2)
        except Exception as e:
            print e

    # 选择来源
    def bsource_select(self, index):
        try:
            self.find_element(self.b_source_label).click()
            self.sleep(1)
            self.click(self.b_source)
            self.sleep(1)
            all_options = self.find_elements(self.bsource_options)
            print len(all_options)
            obj_options = all_options[index]
            print obj_options
            obj_options.click()
        except Exception as e:
            print e

    # 填写备注
    def bnote_input(self, text):
        try:
            self.type(self.b_note, text)
            self.sleep(1)
        except Exception as e:
            print e

    # 选择商品
    def bproduct_select(self, text):
        try:
            self.click(self.b_addproduct)
            self.sleep(2)
            self.click(self.b_clickproduct)
            self.sleep(2)
            self.type(self.b_searchproduct, text)
            self.click(self.b_searchbtn)
            self.sleep(1)
            self.click(self.b_result1)
            self.find_element(self.b_resultbtn).click()
        except Exception as e:
            print e

    # 点击保存按钮
    def click_savebtn(self):
        try:
            self.click(self.b_savebtn)
            self.sleep(3)
        except Exception as e:
            print e

    # 获取新增成功提示信息：新增商机成功！
    def get_b_alert(self, text):
        try:
            self.get_alert(text)
        except Exception as e:
            print e

    # 点击写跟进--取消按钮
    def click_cancelbtn(self):
        try:
            self.find_element(self.b_follow_cbtn).click()
        except Exception as e:
            print e
