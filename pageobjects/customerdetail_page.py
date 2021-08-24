# -*- coding:utf-8 -*-
from framework.base_page import BasePage
import random


class CustomerDetailPage(BasePage):
    # 客户详情页关闭按钮
    cdetail_close_btn = "xpath=>//*[@id='app']/div/div[4]/div/div/i"
    # 客户详情打标签按钮
    addtag_btn = "xpath=>//*[@id='app']/div/div[4]/div/section/div[2]/button[1]"
    # 客户名称列数据
    cname_list = "xpath=>//*[@id='app']/div/div[2]/div/div[4]/div[2]/table/tbody/tr/td[3]/div/div"
    # 打标签弹窗，选择目标标签
    tag_name = "xpath=>//*[@class='tag-dialog-main']/div/div"
    # 打标签弹窗，保存按钮
    tag_save_btn = "xpath=>//*[@id='app']/div/div[4]/div/div[2]/div/main/div[2]/button[1]"
    # 客户详情_联系人tab
    contact_tab = "xpath=>//*[@id='app']/div/div[4]/div/main/div/div[1]/nav[3]"
    # 客户详情_联系人tab_新增联系人按钮
    contact_add_btn = "xpath=>//*[@id='app']/div/div[4]/div/main/div/div[2]/div/div/div[1]/div/div[1]/button[1]"
    # 客户详情_联系人tab_新增联系人弹窗，联系人姓名
    contact_name_input = "xpath=>//*[@id='app']/div/div[4]/div/main/div/div[2]/div/div[2]/div/div/form/div[1]/div[1]/div/div/div/input"
    # 客户详情_联系人tab_新增联系人弹窗，联系人手机
    contact_phone_input = "xpath=>//*[@id='app']/div/div[4]/div/main/div/div[2]/div/div[2]/div/div/form/div[1]/div[2]/div/div/div/input"
    # 客户详情_联系人tab_新增联系人弹窗，联系人职务
    contact_post_input = "xpath=>//*[@id='app']/div/div[4]/div/main/div/div[2]/div/div[2]/div/div/form/div[2]/div[1]/div/div/div/input"
    # 客户详情_联系人tab_新增联系人弹窗，联系人座机
    conntact_landline_input = "xpath=>//*[@id='app']/div/div[4]/div/main/div/div[2]/div/div[2]/div/div/form/div[2]/div[2]/div/div/div/input"
    # 客户详情_联系人tab_新增联系人弹窗，联系人邮箱
    # 客户详情_联系人tab_新增联系人弹窗，联系人微信
    # 客户详情_联系人tab_新增联系人弹窗，联系人QQ
    # 客户详情_联系人tab_新增联系人弹窗，联系人旺旺
    # 客户详情_联系人tab_新增联系人弹窗，联系人备注
    # 客户详情_联系人tab_新增联系人弹窗，保存按钮
    contact_save_btn = "xpath=>//*[@id='app']/div/div[4]/div/main/div/div[2]/div/div[2]/div/div/div/button[1]"

    # 获取客户名称列表数据，按照客户名称选择目标客户，点击进入详情页
    def target_customer(self, cnametext):
        # 获取客户名称列表数据
        try:
            cnamedatas = self.find_elements(self.cname_list)
            for name in cnamedatas:
                if name.text == cnametext:
                    print u"找到目标客户为: %s 。" % name.text
                    name.click()
                else:
                    pass
        except Exception as e:
            print e

    # 点击关闭按钮，关闭详情页
    def close_detailpage(self):
        try:
            self.click(self.cdetail_close_btn)
            self.sleep(1)
        except Exception as e:
            print e

    # 获取提示信息：保存成功
    def get_alert(self, text):
        try:
            if unicode(text) in self.driver.page_source:
                print u"验证通过，系统提示与期望提示'%s'一致。" % text
            else:
                print u"验证失败，系统提示与期望提示'%s'不一致。" % text
        except Exception as e:
            print u"捕捉到异常信息: %s 。" % e

# ---------客户详情-打标签-----------------

    # 点击打标签按钮
    def click_addtag_btn(self):
        try:
            self.click(self.addtag_btn)
            self.sleep(1)
        except Exception as e:
            print e

    # 选择目标标签名
    def check_target_tagname(self, tagname):
        try:
            tags = self.find_elements(self.tag_name)
            for tag in tags:
                if tag.text == tagname:
                    print u"找到目标标签为：%s。" % tag.text
                    tag.click()
                else:
                    pass
        except Exception as e:
            print e

    # 点击保存按钮
    def click_savetag_btn(self):
        try:
            self.click(self.tag_save_btn)
            self.sleep(1)
        except Exception as e:
            print e

# ---------客户详情——联系人tab------------------

    # 切换到客户详情_联系人tab
    def switchto_contact_tab(self):
        try:
            self.click(self.contact_tab)
            self.sleep(1)
        except Exception as e:
            print e

    # 点击新增联系人按钮
    def click_contactbtn(self):
        try:
            self.click(self.contact_add_btn)
            self.sleep(1)
        except Exception as e:
            print e

    # 填写联系人姓名
    def cc_name_input(self, text):
        try:
            self.type(self.contact_name_input, text)
            self.sleep(2)
        except Exception as e:
            print e

    # 填写联系人手机
    def cc_phone_input(self, text):
        try:
            self.type(self.contact_phone_input, text)
            self.sleep(2)
        except Exception as e:
            print e

    # 随机创建手机号
    def RandomPhone(self):
        try:
            prelist = ["130", "131", "132", "133", "134", "135", "136", "137", "138", "139", "147", "150", "151", "152",
                       "153", "155", "156", "157", "158", "159", "186", "187", "188"]
            randomPre = random.choice(prelist)
            Number = "".join(random.choice("0123456789") for i in range(8))
            phoneNum = randomPre + Number
            return phoneNum
        except Exception as e:
            print e

    # 填写联系人职务
    def cc_post_input(self, text):
        try:
            self.type(self.contact_post_input, text)
            self.sleep(2)
        except Exception as e:
            print e

    # 点击联系人信息保存按钮
    def cc_save_btn(self):
        try:
            self.click(self.contact_save_btn)
            self.sleep(1)
        except Exception as e:
            print e
