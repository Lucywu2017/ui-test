# -*- coding: utf-8 -*-
# @Time    : 2017-12-29 13:22
# 充值

from WebPages.ChargeWithdrawBankCardPage import ChargeWithdrawBankCardPage
from ConstantLocate import Constant

# 多次充值
chargeWithdrawBankCardPage = ChargeWithdrawBankCardPage()

class ChargeFunction(ChargeWithdrawBankCardPage):
    @staticmethod
    def charge_money(money, times):
        for i in range(0, times):
            chargeWithdrawBankCardPage.click_my_account()
            chargeWithdrawBankCardPage.click_charge_in_account()
            chargeWithdrawBankCardPage.send_charge_withdraw_amount(money)
            chargeWithdrawBankCardPage.click_submit_charge()
            chargeWithdrawBankCardPage.click_online_pay_button()
            chargeWithdrawBankCardPage.click_agree_button()
            chargeWithdrawBankCardPage.click_go_pay_online()
            chargeWithdrawBankCardPage.close_driver()
            chargeWithdrawBankCardPage.switch_to_window('Insert')
            chargeWithdrawBankCardPage.click_attestation_success()
            chargeWithdrawBankCardPage.accept_alert()


if __name__ == '__main__':
    chargeWithdrawBankCardPage.open(Constant.LoginURL)
    chargeWithdrawBankCardPage.login(Constant.UserName, Constant.Password)
    #每次充值1000，连续充值3次
    ChargeFunction.charge_money(1000, 2)
    chargeWithdrawBankCardPage.quit()
