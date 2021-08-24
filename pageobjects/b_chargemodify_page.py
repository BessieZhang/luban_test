# -*- coding:utf-8 -*-
from framework.base_page import BasePage


# 客户负责人转交相关元素
class BChargePage(BasePage):
    # 查询按钮
    b_search_btn = "xpath=>//*[@id='business-list-container']/div/div/button[1]"
    # 更多查询按钮
    b_searchmore_btn = "xpath=>//*[@id='business-list-container']/div/div/span/button"
    # 更多查询--负责人下拉框
    b_searchmore_charge = "xpath=>//*[@role='tooltip']/div[1]/div/div/form/div[2]/div[1]/div/div/div/div[2]/span"
    # 更多查询--负责人下拉数据
    b_searchmore_charge_options = "xpath=>/html/body/div[3]/div[1]/div[1]/ul/li/span"
    # 勾选框
    b_checkbox = "xpath=>//*[@id='business-container']/div[2]/div/div/div[4]/div[2]/table/tbody/tr[1]/td[2]/div/label"
    # 点击负责人转交按钮
    b_transcharge_btn = "xpath=>//*[@id='business-container']/div[2]/section/div/div/div/div[1]/div/button[2]"
    # 负责人转交窗口--负责人下拉框
    b_transcharge_input = "xpath=>//*[@id='business-container']/div[2]/div[2]/div[1]/main/div[1]/div/div/input"
    # 负责人转交窗口--负责人下拉数据
    b_transcharge_options = "xpath=>/html/body/div[4]/div[1]/div[1]/ul/li/span"
    # 负责人转交窗口--保存按钮
    b_transcharge_savebtn = "xpath=>//*[@id='business-container']/div[2]/div[2]/div[1]/main/div[2]/button[1]"

    # # 按照index搜索负责人的测试数据
    # def search_testdata(self, text):
#         self.click(self.b_searchmore_btn)
#         self.sleep(1)
#         self.find_element(self.b_searchmore_charge).click()
#         self.sleep(1)
#         all_options = self.find_elements(self.b_searchmore_charge_options)
#         for a in range(len(all_options)):
#             if all_options[a].text == text:
#                 obj_option = all_options[a]
#                 obj_option.click()
#                 print obj_option.text
#         self.click(self.b_searchmore_btn)
#         self.sleep(2)

    # 按照英文名搜索负责人的测试数据
    def search_testdata(self, text):
        try:
            self.click(self.b_searchmore_btn)
            self.sleep(1)
            self.search_objoperator(self.b_searchmore_charge, self.b_searchmore_charge_options, text)
            self.sleep(1)
            self.click(self.b_searchmore_btn)
        except Exception as e:
            print e

    # 勾选第一个搜索结果
    def check_firstdata(self):
        try:
            self.find_element(self.b_checkbox).click()
            self.sleep(2)
        except Exception as e:
            print e

    # 点击负责人转交按钮
    def click_bchargebtn(self):
        try:
            self.click(self.b_transcharge_btn)
            self.sleep(2)
        except Exception as e:
            print e

    # 点击负责人下拉框，选择目标负责人
    def bcharge_select(self, text):
        try:
            self.search_objoperator(self.b_transcharge_input, self.b_transcharge_options, text)
            self.sleep(1)
            self.click(self.b_transcharge_savebtn)
        except Exception as e:
            print e

    # 获取提示信息：转交成功！
    def get_tb_alert(self, text):
        try:
            self.get_alert(text)
        except Exception as e:
            print e



