#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017-11-25 13:35
# @Author  : 伍露露
# 充值、提现、银行卡管理相关功能方法

from WebPages.BasePage import BasePage
from selenium.webdriver.support import select
from SelementLocate import PortalObject
import time


class ChargeWithdrawBankCardPage(BasePage):

    #充值页面
    def get_balance_in_charge_withdraw_tab(self):
        """充值提现页面获取可用余额"""
        value = self.driver.find_element(*PortalObject.balanceInChargeWithdrawTab).text
        balance = float(value.strip()[:-1].replace(',', ''))
        return balance

    def send_charge_withdraw_amount(self, amount):
        """输入充值或者提现金额"""
        self.driver.find_element(*PortalObject.chargeInput).send_keys(amount)
        time.sleep(1)

    def click_submit_charge(self):
        """点击立即充值"""
        self.driver.find_element(*PortalObject.submitChargeButton).click()
        time.sleep(3)

    def click_online_pay_button(self):
        """点击网银支付"""
        self.driver.implicitly_wait(5)
        self.driver.find_element(*PortalObject.onlinePayTab).click()

    def click_go_pay_online(self):
        """点击去网银充值"""
        self.driver.find_element(*PortalObject.goPayOnlineButton).click()
        time.sleep(3)

    def click_agree_button(self):
        """点击我同意"""
        self.driver.find_element(*PortalObject.agreeButton).click()
        time.sleep(2)

    def click_attestation_success(self):
        """点击验签成功"""
        self.driver.find_element(*PortalObject.attestationSuccessButton).click()
        time.sleep(2)

    def click_pay_success_button(self):
        """在新浪支付页面点击已完成支付"""
        self.driver.find_element(*PortalObject.paySuccessButton).click()
        time.sleep(8)


    #提现页面
    def click_submit_withdraw(self):
        """点击确认提现"""
        try:
            self.driver.find_element(*PortalObject.submitWithdrawButton).click()
        except Exception:
            self.driver.find_element(*PortalObject.submitWithdrawButton2).click()
        time.sleep(3)

    def is_auto_pop_show(self):
        """温馨提示"""
        try:
            self.driver.find_element(*PortalObject.autoPop).is_displayed()
            return True
        except Exception:
            return False

    def enter_pay_password_in_withdraw(self, password):
        """提现页面的支付密码输入框"""
        self.driver.find_element(*PortalObject.payPswInput).send_keys(password)

    def click_success_withdraw_button(self):
        """点击完成"""
        self.driver.find_element(*PortalObject.submitButton).click()
        time.sleep(10)


    #银行卡管理页面相关
    def click_unbind_button(self):
        """点击解绑按钮"""
        self.driver.implicitly_wait(5)
        self.driver.find_element(*PortalObject.unbindButton).click()
        time.sleep(3)

    def click_withdraw_button_in_pop(self):
        """弹框中点击确认提现"""
        self.driver.find_element(*PortalObject.withdrawButtonInPop).click()
        time.sleep(6)

    def click_submit_withdraw_unbind(self):
        """弹框中点击确认提现"""
        self.driver.find_element(*PortalObject.submitWithdrawButton).click()
        self.driver.find_element(*PortalObject.submitWithdrawButton2).click()
        time.sleep(6)

    def is_bind_bank_card(self):
        """
        是否绑定银行卡
        :return: 
        """
        try:
            self.driver.find_element(*PortalObject.bindCardButton).is_displayed()
            return False
        except BaseException:
            return True

    def enter_bank_card(self, bank_card):
        """输入卡号"""
        self.driver.find_element(*PortalObject.bankCardInput).send_keys(bank_card)

    def click_outside(self):
        """点击输入框外面区域"""
        self.driver.find_element(*PortalObject.outsideArea).click()
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






