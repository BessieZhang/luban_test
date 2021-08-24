# -*- coding:utf-8 -*-
from framework.base_page import BasePage


# 客户负责人转交相关元素
class ChargePage(BasePage):
    # 搜索框
    # c_search_input = "xpath=>//*[@id='search-head']/div/div/div[1]/input"
    # 更多查询按钮
    c_searchmore_btn = "xpath=>//*[@id='search-head']/div/div/div[2]/span/button"
    # 更多查询--销售下拉框
    c_searchmore_sale = "xpath=>//*[@role='tooltip']/div[1]/form/div[3]/div[2]/div/div/div/div[2]/span"
    # 更多查询--销售下拉数据
    c_searchmore_sale_options ="xpath=>//*[@role='tooltip']/div[1]/form/div[3]/div[2]/div/div/div/div[3]/div[1]/div[1]/ul/li/span"
    # 更多查询--协作人下拉框
    c_searchmore_assist = "xpath=>//*[@role='tooltip']/div[1]/form/div[4]/div[1]/div/div/div/div[2]/span"
    # 更多查询--协作人下拉数据
    c_searchmore_assist_options = "xpath=>//*[@role='tooltip']/div[1]/form/div[4]/div[1]/div/div/div/div[3]/div[1]/div[1]/ul/li/span"

    # 查询按钮
    c_search_btn = "xpath=>//*[@id='search-head']/div/div/button[1]"
    # 勾选框
    c_checkbox = "xpath=>//*[@id='app']/div/div[2]/div/div[4]/div[2]/table/tbody/tr[1]/td[2]/div/label"

    # 获取销售信息
    c_sale = "xpath=>//*[@id='app']/div/div[2]/div/div[3]/table/tbody/tr[1]/td[5]/div/div"
    # 获取协作人信息
    c_assist = "xpath=>//*[@id='app']/div/div[2]/div/div[3]/table/tbody/tr[1]/td[6]/div/div"

    # 负责人转交按钮
    c_transcharge_btn = "xpath=>//*[@id='app']/div/section/div/div[1]/div[1]/button"
    # 销售转交按钮
    c_transsale_btn = "xpath=>//*[@id='app']/div/section/div/div[1]/div[1]/div/div[1]"
    # 销售转交窗口--销售下拉框
    c_transsale_input = "xpath=>//*[@id='app']/div/div[4]/div[1]/main/div[1]/div/div/input"
    # 销售转交窗口--销售下拉数据
    c_transsale_options = "xpath=>/html/body/div[3]/div[1]/div[1]/ul/li/span"
    # 销售转交窗口--保存按钮
    c_transsale_savebtn = "xpath=>//*[@id='app']/div/div[4]/div[1]/main/div[2]/button[1]"

    # 添加协作人按钮
    c_transassist_btn = "xpath=>//*[@id='app']/div/section/div/div[1]/div[1]/div/div[2]"
    # 添加协作人窗口--协作人下拉框
    c_transassist_input = "xpath=>//*[@id='app']/div/div[4]/div[2]/main/div[1]/div/div[1]/input"
    # 添加协作人窗口--协作人下拉数据
    c_transassist_options = "xpath=>/html/body/div[5]/div[1]/div[1]/ul/li/span"
    # 添加协作人窗口--保存按钮
    c_transassist_savebtn = "xpath=>//*[@id='app']/div/div[4]/div[2]/main/div[2]/button[1]"

    # 按照index搜索销售的测试数据
    # def search_testdata(self, index):
    #     try:
    #         self.click(self.c_searchmore_btn)
    #         self.sleep(1)
    #         self.find_element(self.c_searchmore_sale).click()
    #         self.sleep(1)
    #         all_options = self.find_elements(self.c_searchmore_sale_options)
    #         # print len(all_options)
    #         obj_option = all_options[index]
    #         obj_option.click()
    #         self.click(self.c_search_btn)
    #         self.sleep(2)
    #     except Exception as e:
    #         print e

    # 按照英文名搜索销售的测试数据
    def search_testdata(self, text):
        try:
            self.click(self.c_searchmore_btn)
            self.sleep(1)
            self.search_objoperator(self.c_searchmore_sale, self.c_searchmore_sale_options, text)
            self.sleep(1)
            self.click(self.c_search_btn)
        except Exception as e:
            print e

    # 按照英文名搜索协作人的测试数据
    def search_atestdata(self, text):
        try:
            self.click(self.c_searchmore_btn)
            self.sleep(1)
            self.search_objoperator(self.c_searchmore_assist, self.c_searchmore_assist_options, text)
            self.sleep(1)
            self.click(self.c_search_btn)
        except Exception as e:
            print e

    # 勾选第一个搜索结果
    def check_firstdata(self):
        try:
            self.find_element(self.c_checkbox).click()
            self.sleep(2)
        except Exception as e:
            print e

    # 获取销售信息
    def get_saleinfo(self):
         try:
            saleinfo = self.find_element(self.c_sale)
            print saleinfo.text
            return saleinfo.text
         except Exception as e:
            print e

    # 获取协作人信息
    def get_assistinfo(self):
         try:
            assistinfo = self.find_element(self.c_assist)
            print assistinfo.text
            return assistinfo.text
         except Exception as e:
            print e

    # 点击负责人转交--销售转交按钮
    def click_chargebtn(self):
        try:
            self.click(self.c_transcharge_btn)
            self.sleep(1)
            self.find_element(self.c_transsale_btn).click()
            self.sleep(1)
        except Exception as e:
            print e

    # 点击销售下拉框，选择目标销售
    # def charge_select(self, index):
    #     try:
    #         self.click(self.c_transsale_input)
    #         self.sleep(1)
    #         all_options = self.find_elements(self.c_transsale_options)
    #         # print len(all_options)
    #         obj_option = all_options[index]
    #         obj_option.click()
    #         self.sleep(1)
    #         self.click(self.c_transsale_savebtn)
    #     except Exception as e:
    #         print e

    def charge_saleselect(self, text):
        try:
            self.search_objoperator(self.c_transsale_input, self.c_transsale_options, text)
            self.sleep(1)
            self.click(self.c_transsale_savebtn)
        except Exception as e:
            print e

    # 点击协作人下拉框，选择目标协作人
    def charge_assistselect(self, text):
        try:
            self.search_objoperator(self.c_transassist_input, self.c_transassist_options, text)
            self.sleep(1)
            self.click(self.c_transassist_savebtn)
        except Exception as e:
            print e

    # 获取转交负责人成功提示信息：保存成功
    def get_t_alert(self, text):
        try:
            self.get_alert(text)
        except Exception as e:
            print e
