# -*- coding: utf-8 -*-
# @Time    : 2017-11-21 13:35
# @Author  : 伍露露
# 注册、实名认证、绑卡、设置支付密码相关功能方法

from WebPages.BasePage import BasePage
from CommonLibrary.Util import get_sms
from SelementLocate import PortalObject
from selenium.webdriver.support import select
import time


class NewUserCertificationPage(BasePage):
    #Step1: 注册
    def new_user_register(self, username, password):
        self.click_register_button()
        self.input_username(username)
        self.input_password(password)
        self.get_verify_code()
        #获取验证码

        verify_code = get_sms(username)
        self.enter_verify_code(verify_code)
        self.click_register_confirm_button()
        time.sleep(3)

    def click_register_button(self):
        """点击注册领红包按钮"""
        self.driver.find_element(*PortalObject.registerButton).click()

    def get_verify_code(self):
        """点击获取验证码按钮"""
        self.driver.find_element(*PortalObject.verifyCodeButton).click()
        time.sleep(3)

    def enter_verify_code(self, verify_code):
        """输入短信验证码"""
        self.driver.find_element(*PortalObject.verifyCodeInput).send_keys(verify_code)

    def click_register_confirm_button(self):
        """点击注册并领取1888元新人礼包按钮"""
        self.driver.find_element(*PortalObject.registerConfirmButton).click()
        time.sleep(3)

    #获取页面错误信息
    # def is_error_message_show(self):
    #     try:
    #       if not self.find_element(*PortalObject.errorMessage).is_displayed():
    #           return \
    #               false
    #     except:
    #         self.driver.save_screenshot('/Attachment/validate_error.png')
    #         return false


    #Step2: 实名认证
    def click_realname_button(self):
        """点击我的账户中的立即认证按钮"""
        self.driver.find_element(*PortalObject.realnameButton).click()

    def enter_realname(self, realname):
        """输入姓名"""
        self.driver.find_element(*PortalObject.realnameInput).send_keys(realname)

    def enter_id_card(self, id_card):
        """输入身份证号"""
        self.driver.find_element(*PortalObject.idCardInput).send_keys(id_card)

    def click_realname_cert_button(self):
        """点击账户安全的立即认证按钮"""
        self.driver.find_element(*PortalObject.realnameCertButton).click()
        time.sleep(5)



    #Step3: 绑卡页面
    def enter_bank_card(self, bank_card):
        """输入卡号"""
        self.driver.find_element(*PortalObject.bankCardInput).send_keys(bank_card)

    def click_outside(self):
        """点击输入框外面区域"""
        self.driver.find_element(*PortalObject.phoneNoInput).click()
        time.sleep(3)

    def get_bank_type(self):
        """获取卡号类型信息"""
        bank_type = self.driver.find_element(*PortalObject.bankType).text
        print("卡号类型：" + bank_type)
        return bank_type

    def select_province(self, province):
        """选择省份"""
        sel = self.driver.find_element(*PortalObject.provinceSelect)
        select.Select(sel).select_by_value(province)
        time.sleep(1)

    def select_city(self, city):
        """选择市"""
        sel = self.driver.find_element(*PortalObject.citySelect)
        select.Select(sel).select_by_value(city)
        time.sleep(1)

    def enter_phone_bank(self, bank_phone):
        """填写银行预留手机号"""
        self.driver.find_element(*PortalObject.phoneNoInput).send_keys(bank_phone)

    def click_get_valid_code_in_bind_card(self):
        """点击绑卡页面的获取手机验证码按钮"""
        self.driver.find_element(*PortalObject.getValidCodeButInBindCard).click()

    def enter_valid_code_in_bind_card(self, valid_code):
        """输入获取到的手机验证码"""
        self.driver.find_element(*PortalObject.validCodeInputInBindCard).send_keys(valid_code)

    def click_bank_card_submit_button(self):
        """点击立即绑定按钮"""
        self.driver.find_element(*PortalObject.bankCardSubmitBut).click()
        time.sleep(3)

    # Step4: 设置支付密码
    def click_set_pay_password_button(self):
        """点击设置支付密码按钮"""
        self.driver.find_element(*PortalObject.setPayPswButton).click()
        time.sleep(3)

    def enter_phone_in_bank(self, mobile_number):
        """填写银行预留手机号"""
        self.driver.find_element(*PortalObject.phoneInBankInput).send_keys(mobile_number)

    def click_get_valid_code_in_set_psw(self):
        """填写银行预留手机号"""
        self.driver.find_element(*PortalObject.getValidCodeButInSetPsw).click()

    def enter_valid_code_in_set_psw(self, valid_code):
        """输入验证码"""
        self.driver.find_element(*PortalObject.validCodeInputInSetPsw).send_keys(valid_code)

    def enter_pay_psw_in_set_psw(self, valid_code):
        """输入支付密码"""
        self.driver.find_element(*PortalObject.setPswInputInSetPsw).send_keys(valid_code)

    def enter_pay_psw_again_in_set_psw(self, valid_code):
        """再次输入支付密码"""
        self.driver.find_element(*PortalObject.setPswInputInSetPsw).send_keys(valid_code)

    def click_submit_button(self):
        """点击确认按钮"""
        self.driver.find_element(*PortalObject.submitButton).click()
        time.sleep(3)







