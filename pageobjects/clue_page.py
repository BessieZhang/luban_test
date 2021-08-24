# -*- coding:utf-8 -*-
from framework.base_page import BasePage


class CluePage(BasePage):
    # 线索管理菜单
    clue_manage = "xpath=>//*[@id='menuBar']/li[2]"
    # 线索列表菜单
    clue_list = "xpath=>//*[@id='menuBar']/li[2]/ul/li[2]"
    # 关键词搜索框
    keywords_input = "xpath=>//*[@id='app']/div/div[1]/div/div[1]/div[1]/div[1]/div/input"
    # 查询按钮
    search_btn = "xpath=>//*[@id='app']/div/div[1]/div/div[2]/button[1]"
    # 搜索结果_线索编号
    result_id = "xpath=>//*[@id='app']/div/div[2]/div[2]/div[3]/table/tbody/tr[1]/td[3]/div/div"
    # 线索详情_关联商机tab
    relation_btn = "xpath=>//*[@id='app']/div/div[3]/div/div/div[2]/main/div[1]/nav[3]"
    # 关联已有客户
    existing_customers = "xpath=>//*[@id='app']/div/div[3]/div/div/div[2]/main/div[2]/div/div/div/div/div/div/div/div[2]"
    # 线索转化按钮
    clue_transferbtn = "xpath=>//*[@id='app']/div/div[3]/div/div/div[2]/main/div[2]/div/div/div/div/div/div/button"

    # 线索转化弹窗_客户搜索框
    customer_search_input = "xpath=>//*[@id='app']/div/div[3]/div/div/div[2]/main/div[2]/div/div/div/div/div[2]/div/div[2]/div/div/div[1]/div/div/div/input"
    # 线索转化弹窗_确定按钮
    customer_search_btn = "xpath=>//*[@id='app']/div/div[3]/div/div/div[2]/main/div[2]/div/div/div/div/div[2]/div/div[2]/div/div/div[1]/div/div/button"
    # 线索转化弹窗_搜索已有客户结果
    search_result_checkbox = "xpath=>//*[@id='app']/div/div[3]/div/div/div[2]/main/div[2]/div/div/div/div/div[2]/div/div[2]/div/div/div[3]/div/div[3]/table/tbody/tr/td[2]/div/label/span/span"
    # 线索转化弹窗_客户_下一步
    clue_transfer_customer_next = "xpath=>//*[@id='app']/div/div[3]/div/div/div[2]/main/div[2]/div/div/div/div/div[2]/div/div[3]/button"

    # 线索转化弹窗_联系人_关联现有联系人按钮
    clue_related_existing_contact = "xpath=>//*[@id='app']/div/div[3]/div/div/div[2]/main/div[2]/div/div/div/div/div[2]/div/div[2]/div/div[1]/label[2]/span[1]"
    # 线索转化弹窗_联系人_联系人列表第一个数据
    contact_checkbox = "xpath=>//*[@id='app']/div/div[3]/div/div/div[2]/main/div[2]/div/div/div/div/div[2]/div/div[2]/div/div[2]/div/div/div[3]/table/tbody/tr/td[2]/div/label/span/span"
    # 线索转化弹窗_联系人_下一步
    clue_transfer_contact_next = "xpath=>//*[@id='app']/div/div[3]/div/div/div[2]/main/div[2]/div/div/div/div/div[2]/div/div[3]/button[2]"

    # 线索转化弹窗_商机_商机标题下拉框
    clue_business_title = "xpath=>//*[@id='app']/div/div[3]/div/div/div[2]/main/div[2]/div/div/div/div/div[2]/div/div[2]/div/div/div/div/form/div[1]/div[1]/div/div/div/div[1]/input"
    # 线索转化弹窗_商机_商机标题下拉数据
    clue_business_title_options = "xpath=>/html/body/div[2]/div[1]/div[1]/ul/li/span"
    # 线索转化弹窗_商机_空白区域，失焦以收起下拉框
    clue_space = "xpath=>//*[@id='app']/div/div[3]/div/div/div[2]/main/div[2]/div/div/div/div/div[2]/div/div[2]/div/div/div/div/form/div[1]/div[2]/div/label"
    # 预计成交日期框
    clue_business_date = "xpath=>//*[@id='app']/div/div[3]/div/div/div[2]/main/div[2]/div/div/div/div/div[2]/div/div[2]/div/div/div/div/form/div[2]/div[2]/div/div/div/input"
    # 预计成交日期 9-30
    clue_deal_date = "xpath=>/html/body/div[3]/div[1]/div/div[2]/table[1]/tbody/tr[6]/td[4]/div/span"
    # 负责人下拉框
    charge_select = "xpath=>//*[@id='app']/div/div[3]/div/div/div[2]/main/div[2]/div/div/div/div/div[2]/div/div[2]/div/div/div/div/form/div[3]/div[1]/div/div/div/div[1]/input"
    # 负责人下拉数据
    charge_options = "xpath=>/html/body/div[4]/div[1]/div[1]/ul/li/span"
    # 协作人下拉框
    assistant_select = "xpath=>//*[@id='app']/div/div[3]/div/div/div[2]/main/div[2]/div/div/div/div/div[2]/div/div[2]/div/div/div/div/form/div[3]/div[2]/div/div/div/div[2]/span/span"
    # 协作人下拉数据
    assistant_options = "xpath=>/html/body/div[6]/div[1]/div[1]/ul/li/span"
    # 来源下拉框
    source_select = "xpath=>//*[@id='app']/div/div[3]/div/div/div[2]/main/div[2]/div/div/div/div/div[2]/div/div[2]/div/div/div/div/form/div[4]/div/div/div/div[1]/input"
    # 来源下拉数据_搜索结果：平台订购 /html/body/div[5]/div[2]/div[1]/ul/li
    source_result = "xpath=>/html/body/div[6]/div[2]/div[1]/ul/li/span"
    # 备注文本框
    remark_textarea = "xpath=>//*[@id='app']/div/div[3]/div/div/div[2]/main/div[2]/div/div/div/div/div[2]/div/div[2]/div/div/div/div/form/div[5]/div/div/textarea"
    # 新增商品按钮
    product_addbtn = "xpath=>//*[@id='app']/div/div[3]/div/div/div[2]/main/div[2]/div/div/div/div/div[2]/div/div[2]/div/div/div/div/div/div/div[1]/button"

    # 点击线索管理菜单
    def click_cmbtn(self):
        try:
            self.click(self.clue_manage)
            self.sleep(2)
        except Exception as e:
            print e

    # 点击线索列表菜单
    def click_clbtn(self):
        try:
            self.click(self.clue_list)
            self.sleep(2)
        except Exception as e:
            print e

    # 切换到线索列表iframe中
    def switch_iframe1(self):
        try:
            self.switch_iframe(1)
            self.sleep(2)
        except Exception as e:
            print e

    # 查询关键词
    def search_clue(self, text):
        try:
            self.type(self.keywords_input, text)
            self.sleep(1)
        except Exception as e:
            print e

    # 点击查询按钮
    def click_searchbtn(self):
        try:
            self.click(self.search_btn)
            self.sleep(1)
        except Exception as e:
            print e

    # 点击线索编号进入线索详情
    def click_resultid(self):
        try:
            self.click(self.result_id)
            self.sleep(1)
        except Exception as e:
            print e

    # 点击关联商机tab按钮
    def click_relationtab(self):
        try:
            self.click(self.relation_btn)
            self.sleep(1)
        except Exception as e:
            print e

    # 点击关联已有客户区域
    def click_relateexistingcustomer(self):
        try:
            self.click(self.existing_customers)
            self.sleep(1)
        except Exception as e:
            print e

    # 点击线索转化按钮
    def click_cluetransfer_btn(self):
        try:
            self.click(self.clue_transferbtn)
            self.sleep(2)
        except Exception as e:
            print e

    # 查询已有客户
    def search_existing_customer(self, text):
        try:
            self.type(self.customer_search_input, text)
            self.sleep(1)
        except Exception as e:
            print e

    # 点击确定按钮
    def click_surebtn(self):
        try:
            self.click(self.customer_search_btn)
            self.sleep(1)
        except Exception as e:
            print e

    # 勾选客户搜索结果
    def check_customer(self):
        try:
            self.click(self.search_result_checkbox)
            self.sleep(1)
        except Exception as e:
            print e

    # 点击客户_下一步按钮
    def click_customer_next(self):
        try:
            self.click(self.clue_transfer_customer_next)
            self.sleep(1)
        except Exception as e:
            print e

    # 点击关联现有联系人按钮
    def click_existing_contact(self):
        try:
            self.click(self.clue_related_existing_contact)
            self.sleep(1)
        except Exception as e:
            print e

    # 勾选现有联系人第一个数据
    def check_contact(self):
        try:
            self.click(self.contact_checkbox)
            self.sleep(1)
        except Exception as e:
            print e

    # 点击联系人_下一步按钮
    def click_contact_next(self):
        try:
            self.click(self.clue_transfer_contact_next)
            self.sleep(1)
        except Exception as e:
            print e

    # 选择商机标题
    def choose_business_title(self, *args):
        try:
            self.click(self.clue_business_title)
            self.sleep(1)
            all_options = self.find_elements(self.clue_business_title_options)
            print len(all_options)
            for a in args:
                all_options[a].click()
            self.sleep(1)
        except Exception as e:
            print e
        self.click(self.clue_space)

    # 预计成交日期
    def choose_dealdate(self):
        try:
            self.click(self.clue_business_date)
            self.click(self.clue_deal_date)
            self.sleep(1)
        except Exception as e:
            print e

    # 商机负责人
    def bcharge_select(self, *args):
        try:
            self.click(self.charge_select)
            self.sleep(1)
            all_options = self.find_elements(self.charge_options)
            print len(all_options)
            for a in args:
                all_options[a].click()
            self.sleep(2)
        except Exception as e:
            print e

    # 商机协作人
    def bassistant_select(self, *args):
        try:
            self.click(self.assistant_select)
            self.sleep(1)
            all_options = self.find_elements(self.assistant_options)
            print len(all_options)
            for a in args:
                all_options[a].click()
            self.sleep(2)
        except Exception as e:
            print e

    # 商机来源
    def bsource_select(self, text):
        try:
            self.type(self.source_select, text)
            self.click(self.source_result)
            self.sleep(1)
        except Exception as e:
            print e

    # 商机备注
    def bremark_input(self, text):
        try:
            self.type(self.remark_textarea, text)
            self.sleep(1)
        except Exception as e:
            print e

    # 新增商品
    def bproduct_add(self):
        try:
            self.click(self.product_addbtn)
            self.sleep(1)
        except Exception as e:
            print e
