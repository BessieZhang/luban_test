# -*- coding:utf-8 -*-
from framework.base_page import BasePage
import random


class FirstPage(BasePage):
    # 我知道了弹窗
    small_window = "xpath=>/html/body/div[5]/div[3]/c-button"
    # 客户管理菜单
    customer_manage = "xpath=>//*[@id='menuBar']/li[1]"
    # 客户列表菜单
    customer_list = "xpath=>//*[@id='menuBar']/li[1]/ul/li[1]"
    # iframe
    iframe1 = "xpath=>//*[@id='tabsetMain']/contents/content[1]/c-iframe/iframe"
    # 新增客户按钮
    # ================== 客户 ==================
    add_customer = "xpath=>//*[@id='app']/div/section/div/div[1]/button[1]"
    # 客户名称文本框
    c_name = "xpath=>//*[@id='app']/div/div[3]/div/div[2]/div[1]/div/form/div[1]/div[1]/div/div/div/input"
    # 客户联系人文本框
    c_contact = "xpath=>//*[@id='app']/div/div[3]/div/div[2]/div[1]/div/form/div[1]/div[2]/div/div/div/input"
    # 手机文本框
    c_phone = "xpath=>//*[@id='app']/div/div[3]/div/div[2]/div[1]/div/form/div[2]/div[1]/div/div/div/input"
    # 来源下拉框
    c_source = "xpath=>//*[@id='app']/div/div[3]/div/div[2]/div[1]/div/form/div[2]/div[2]/div/div/div/div/div[1]/input"
    # 初次新增客户--来源下拉数据列表
    source_options_o = "xpath=>/html/body/div[2]/div[1]/div[1]/ul/li/span"
    # 二次新增客户--来源下拉数据列表
    source_options_t = "xpath=>/html/body/div[3]/div[1]/div[1]/ul/li/span"
    # 销售下拉框
    c_sales = "xpath=>//*[@id='app']/div/div[3]/div/div/form/div[3]/div[1]/div/div/div/div/span"
    # 销售下拉数据列表
    sale_options = "xpath=>/html/body/div[2]/div[1]/div[1]/ul/li/span"
    # 协作人下拉框
    c_assistants = "xpath=>//*[@id='app']/div/div[3]/div/div[2]/div[1]/div/form/div[3]/div[2]/div/div/div/div[1]/input"
    # 协作人下拉数据列表
    assistant_options = "xpath=>/html/body/div[4]/div[1]/div[1]/ul/li/span"
    # 国家下拉框
    c_country = "xpath=>//*[@id='app']/div/div[3]/div/div[2]/div[1]/div/form/div[4]/div[1]/div/div/div/div[1]/input"
    # 国家下拉数据列表
    country_options = "xpath=>/html/body/div[5]/div[1]/div[1]/ul/li/span"
    # 省份下拉框
    c_province = "xpath=>//*[@id='app']/div/div[3]/div/div[2]/div[1]/div/form/div[4]/div[2]/div/div/div/div[1]/input"
    # 省份下拉列表数据
    province_options = "xpath=>/html/body/div[6]/div[1]/div[1]/ul/li[1]/span"
    # 城市下拉框
    c_city = "xpath=>//*[@id='app']/div/div[3]/div/div[2]/div[1]/div/form/div[5]/div[1]/div/div/div/div[1]/input"
    # 城市下拉列表数据
    city_options = "xpath=>/html/body/div[7]/div[1]/div[1]/ul/li/span"
    # 地区下拉框
    c_area = "xpath=>//*[@id='app']/div/div[3]/div/div[2]/div[1]/div/form/div[5]/div[2]/div/div/div/div/input"
    # 地区下拉列表数据
    area_options = "xpath=>/html/body/div[8]/div[1]/div[1]/ul/li[1]/span"
    # 详细地址文本框
    c_address = "xpath=>//*[@id='app']/div/div[3]/div/div[2]/div[1]/div/form/div[6]/div/div/input"
    # 行业下拉框
    c_profession = "xpath=>//*[@id='app']/div/div[3]/div/div[2]/div[1]/div/form/div[7]/div[1]/div/div/div/div[1]/input"
    # 行业下拉列表数据
    profession_options = "xpath=>/html/body/div[9]/div[1]/div[1]/ul/li/span"
    # 品牌文本框
    # 人员规模下拉框
    c_scale = "xpath=>//*[@id='app']/div/div[3]/div/div[2]/div[1]/div/form/div[8]/div[2]/div/div/div/div[1]/input"
    # 人员规模下拉列表数据
    scale_options = "xpath=>/html/body/div[10]/div[1]/div[1]/ul/li/span"
    # 年销售额下拉框
    c_annualsales = "xpath=>//*[@id='app']/div/div[3]/div/div[2]/div[1]/div/form/div[8]/div[1]/div/div/div/div[1]/input"
    # 年销售额下拉列表数据
    annualsales_options = "xpath=>/html/body/div[11]/div[1]/div[1]/ul/li/span"
    # 邮箱文本框
    c_email = "xpath=>//*[@id='app']/div/div[3]/div/div[2]/div[1]/div/form/div[9]/div[1]/div/div/div/input"
    # 座机文本框
    # c_phonecall = "xpath=>//*[@id='app']/div/div[3]/div/div[2]/div[1]/div/form/div[9]/div[2]/div/div/div/input"
    # 传真文本框
    # c_fax = "xpath=>//*[@id='app']/div/div[3]/div/div/form/div[9]/div[2]/div/div/div/input"
    # 备注文本框
    c_remark = "xpath=>//*[@id='app']/div/div[3]/div/div[2]/div[1]/div/form/div[10]/div/div/textarea"
    # 下一步按钮
    c_next = "xpath=>//*[@id='app']/div/div[3]/div/div[3]/button/span"

    # ================== 商机 ==================
    # 保存按钮
    c_savebtn = "xpath=>//*[@id='app']/div/div[3]/div/div/div/button[1]"
    # 取消按钮
    c_cancelbtn = "xpath=>//*[@id='app']/div/div[3]/div/div/div/button[2]"
    # 客户名称列数据
    cname_list = "xpath=>//*[@id='app']/div/div[2]/div/div[4]/div[2]/table/tbody/tr/td[3]/div/div"
    # 报错提示框
    el_alert = "class_name=>el-message-error"

    # 客户详情--客户信息tab
    c_info = "xpath=>//*[@id='app']/div/div[4]/div/main/div/div[1]/nav[2]"
    # 客户信息--查看按钮
    c_showinfo_btn = "xpath=>//*[@id='app']/div/div[4]/div/main/div/div[2]/div/div[1]/div/div/div/button"
    # 客户手机号码
    c_info_phone = "xpath=>//*[@id='app']/div/div[4]/div/main/div/div[2]/div/div[2]/div[2]/div[1]/em"
    # 客户详情--关闭按钮
    c_info_closebtn = "xpath=>//*[@id='app']/div/div[4]/div/div/i"

    # 点击我知道了关闭弹窗
    def click_swbtn(self):
        try:
            self.click(self.small_window)
            self.sleep(1)
        except:
            print "ignore the button"
            pass

    # 点击客户管理菜单
    def click_cmbtn(self):
        try:
            self.click(self.customer_manage)
            self.sleep(1)
        except Exception as e:
            print e

    # 点击客户列表菜单
    def click_clbtn(self):
        try:
            self.click(self.customer_list)
            self.sleep(2)
        except Exception as e:
            print e

    # 切换到客户列表iframe中
    def switch_iframe1(self):
        try:
            self.switch_iframe(1)
            self.sleep(2)
        except Exception as e:
            print e

    # 点击新增客户按钮
    def click_addbtn(self):
        try:
            self.click(self.add_customer)
            self.sleep(2)
        except Exception as e:
            print e

    # 输入客户名称
    def cname_input(self, text):
        try:
            self.type(self.c_name, text)
            self.sleep(2)
        except Exception as e:
            print e

    # 输入客户联系人
    def ccontact_input(self, text):
        try:
            self.type(self.c_contact, text)
            self.sleep(2)
        except Exception as e:
            print e

    # 输入客户手机
    def cphone_input(self, text):
        try:
            self.type(self.c_phone, text)
            self.sleep(2)
        except Exception as e:
            print e

    # 初次新增客户--点击来源展开下拉框并选择某项
    # def csource_select(self, index):
    #     try:
    #         self.click(self.c_source)
    #         self.sleep(1)
    #         all_options = self.find_elements(self.source_options_o)
    #         obj_option = all_options[index]
    #         obj_option.click()
    #         self.sleep(2)
    #     except Exception as e:
    #         print e
    def csource_select(self, text):
        try:
            self.search_objoperator(self.c_source, self.source_options_o, text)
        except Exception as e:
            print e

    # 二次新增客户--点击来源展开下拉框并选择某项
    def csource_select_t(self, index):
        try:
            self.click(self.c_source)
            self.sleep(1)
            all_options = self.find_elements(self.source_options_t)
            obj_option = all_options[index]
            obj_option.click()
            self.sleep(2)
        except Exception as e:
            print e

    # 点击销售展开下拉框并选择某项
    def csale_select(self, index):
        try:
            self.click(self.c_sales)
            self.sleep(1)
            all_options = self.find_elements(self.sale_options)
            obj_option = all_options[index]
            obj_option.click()
            self.sleep(2)
        except Exception as e:
            print e

    # 点击协作人展开下拉框并选择某几项
    # def cassistant_select(self, *args):
    #     try:
    #         self.click(self.c_assistants)
    #         self.sleep(1)
    #         all_options = self.find_elements(self.assistant_options)
    #         print all_options
    #         for a in args:
    #             all_options[a].click()
    #         self.sleep(2)
    #     except Exception as e:
    #         print e
    def cassistant_select(self, text):
        try:
            self.search_objoperator(self.c_assistants, self.assistant_options, text)
            self.sleep(1)
        except Exception as e:
            print e

    # 选择国家，当前只有中国
    def ccountry_select(self, index):
        try:
            self.click(self.c_country)
            self.sleep(1)
            # all_options = self.find_element(self.country_options)
            # obj_option = all_options[index]
            obj_option = self.find_element(self.country_options)
            print obj_option
            obj_option.click()
        except Exception as e:
            print e

    # 选择省份
    # def cprovince_select(self, index):
    #     try:
    #         self.click(self.c_province)
    #         self.sleep(1)
    #         all_options = self.find_elements(self.province_options)
    #         obj_option = all_options[index]
    #         print obj_option
    #         obj_option.click()
    #     except Exception as e:
    #         print e

    def cprovince_select(self, text):
        try:
            self.search_objoperator(self.c_province, self.province_options, text)
            self.sleep(1)
        except Exception as e:
            print e

    # 选择城市
    # def ccity_select(self, index):
    #     try:
    #         self.click(self.c_city)
    #         self.sleep(1)
    #         all_options = self.find_elements(self.city_options)
    #         obj_option = all_options[index]
    #         print obj_option
    #         obj_option.click()
    #     except Exception as e:
    #         print e

    def ccity_select(self, text):
        try:
            self.search_objoperator(self.c_city, self.city_options, text)
            self.sleep(1)
        except Exception as e:
            print e

    # 选择地区
    # def carea_select(self, index):
    #     try:
    #         self.click(self.c_area)
    #         self.sleep(1)
    #         all_options = self.find_elements(self.area_options)
    #         obj_option = all_options[index]
    #         print obj_option
    #         obj_option.click()
    #     except Exception as e:
    #         print e

    def carea_select(self, text):
        try:
            self.search_objoperator(self.c_area, self.area_options, text)
            self.sleep(1)
        except Exception as e:
            print e

    # 填写详细地址
    def caddress_input(self, text):
        try:
            self.type(self.c_address, text)
            self.sleep(2)
        except Exception as e:
            print e

    # 选择行业
    # def cprofession_select(self, index):
    #     try:
    #         self.click(self.c_profession)
    #         self.sleep(1)
    #         all_options = self.find_elements(self.profession_options)
    #         obj_option = all_options[index]
    #         print obj_option
    #         obj_option.click()
    #     except Exception as e:
    #         print e

    def cprofession_select(self, text):
        try:
            self.search_objoperator(self.c_profession, self.profession_options, text)
            self.sleep(1)
        except Exception as e:
            print e

    # 选择人员规模
    # def cscale_select(self, index):
    #     try:
    #         self.click(self.c_scale)
    #         self.sleep(1)
    #         all_options = self.find_elements(self.scale_options)
    #         obj_options = all_options[index]
    #         print obj_options
    #         obj_options.click()
    #     except Exception as e:
    #         print e

    def cscale_select(self, text):
        try:
            self.search_objoperator(self.c_scale, self.scale_options, text)
            self.sleep(1)
        except Exception as e:
            print e

    # 选择年销售额
    # def cannualsale_select(self, index):
    #     try:
    #         self.click(self.c_annualsales)
    #         self.sleep(1)
    #         all_options = self.find_elements(self.annualsales_options)
    #         obj_options = all_options[index]
    #         print obj_options
    #         obj_options.click()
    #     except Exception as e:
    #         print e

    def cannualsale_select(self, text):
        try:
            self.search_objoperator(self.c_annualsales, self.annualsales_options, text)
            self.sleep(1)
        except Exception as e:
            print e

    # 填写邮箱
    def cemail_input(self, text):
        try:
            self.type(self.c_email, text)
            self.sleep(2)
        except Exception as e:
            print e

    # 填写座机
    def cphonecall_input(self, text):
        try:
            self.type(self.c_phonecall, text)
            self.sleep(2)
        except Exception as e:
            print e

    # 填写传真
    def cfax_input(self, text):
        try:
            self.type(self.c_fax, text)
            self.sleep(2)
        except Exception as e:
            print e

    # 填写备注
    def cremark_input(self, text):
        try:
            self.type(self.c_remark, text)
            self.sleep(2)
        except Exception as e:
            print e

    # 点击下一步按钮
    def click_nextbtn(self):
        try:
            self.click(self.c_next)
            self.sleep(3)
        except Exception as e:
            print e

    # 点击保存按钮
    def click_savebtn(self):
        try:
            self.click(self.c_savebtn)
            self.sleep(3)
        except Exception as e:
            print e

    # 点击取消按钮
    def click_cancelbtn(self):
        try:
            self.click(self.c_cancelbtn)
            self.sleep(1)
        except Exception as e:
            print e

    # 获取客户名称列表数据，判断新增客户是否在列表中
    def get_cnamedata(self, cnametext):
        # 获取客户名称列表数据
        try:
            cnamedatas = self.find_elements(self.cname_list)
            for name in cnamedatas:
                if name.text == cnametext:
                    print u"新增成功！在客户列表中找到新增客户: %s 。" %name.text
                else:
                    pass
        except Exception as e:
            print e

    # 获取客户名称列表中的第一个数据，作为重复客户名称测试数据
    def get_firstdata(self):
        try:
            cnamedatas = self.find_elements(self.cname_list)
            firstdata = cnamedatas[0]
            print u"获取列表中第一个客户名称：%s" %firstdata.text
            return firstdata.text
        except Exception as e:
            print e

    # 获取报错提示信息：客户名称重复
    def get_c_alert(self, text):
        try:
            self.get_alert(text)
        except Exception as e:
            print e

    # 随机创建手机号
    def RandomPhone(self):
        try:
            prelist = ["130", "131", "132", "133", "134", "135", "136", "137", "138", "139", "147", "150", "151", "152",
                       "153", "155", "156", "157", "158", "159", "186", "187", "188"]
            randomPre = random.choice(prelist)
            Number = "".join(random.choice("0123456789") for i in range(8))
            phoneNum = randomPre +Number
            return phoneNum
        except Exception as e:
            print e

    # 关闭客户详情
    def close_cinfo(self):
        try:
            self.click(self.c_info_closebtn)
            self.sleep(2)
        except Exception as e:
            print e

    # 获取客户列表中第一个数据的手机号，作为重复手机号码测试数据
    def get_firstdata_phone(self):
        try:
            first_customer = self.find_elements(self.cname_list)[0]
            print first_customer.text
            first_customer.click()
            self.sleep(2)
            self.click(self.c_info)
            # self.find_element(self.c_info).click()
            self.click(self.c_showinfo_btn)
            self.sleep(2)
            first_phone = self.find_element(self.c_info_phone)
            print first_phone.text
            return first_phone.text
        except Exception as e:
            print e


