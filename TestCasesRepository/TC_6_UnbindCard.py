# -*- coding: utf-8 -*-
# @Time    : 2018-01-18 17:20
# @Author  : 伍露露
# 解绑卡功能测试

import unittest
import CommonLibrary.CommonConfiguration as cc
from CommonLibrary.LogUtility import LogUtility
from CommonLibrary.TestReport import TestReport
from CommonLibrary.TestCaseInfo import TestCaseInfo
from WebPages.ChargeWithdrawBankCardPage import ChargeWithdrawBankCardPage
from ConstantLocate import Constant


class TestUnbindCard(unittest.TestCase):

    def setUp(self):
        self.test_case_info = TestCaseInfo(id=6, name="Test Unbind Card", author='Automation', result='Failed', start_time=cc.get_current_time())
        self.test_report = TestReport(self.test_case_info)
        self.logger = LogUtility()
        self.logger.create_logger_file('Test_Unbind_Card')

    def test_unbind_card(self):
        try:
            # Step1: 登录
            chargeWithdrawBankCardPage = ChargeWithdrawBankCardPage()
            chargeWithdrawBankCardPage.open(Constant.LoginURL)
            chargeWithdrawBankCardPage.login(Constant.UserName, Constant.Password)

            # Step2:到我的账户查看可用余额
            chargeWithdrawBankCardPage.click_my_account()
            balance = chargeWithdrawBankCardPage.get_balance_in_account()

            # Step3: 在银行卡管理页面解绑卡
            chargeWithdrawBankCardPage.click_bank_card_manage_on_left_panel()
            chargeWithdrawBankCardPage.click_unbind_button()

            #如果账户的余额不为0，需要先全部提现再解绑卡
            if balance.__ge__(0.0):
                chargeWithdrawBankCardPage.click_withdraw_button_in_pop()
                self.assertTrue(chargeWithdrawBankCardPage.get_current_url().__contains__("withdraw"))
                chargeWithdrawBankCardPage.click_submit_withdraw_unbind()
                chargeWithdrawBankCardPage.enter_pay_password_in_withdraw(Constant.Password)
                chargeWithdrawBankCardPage.click_success_withdraw_button()
                chargeWithdrawBankCardPage.click_unbind_button()
            else:
                #如果账户的余额为0，直接解绑成功
                self.assertFalse(chargeWithdrawBankCardPage.is_bind_bank_card())

            # All case is passed
            self.test_case_info.result = "Pass"

        except Exception as err:
            self.test_case_info.error_info = str(err)
            self.logger.log(("Got error: "+str(err)))
        finally:
            self.test_case_info.end_time = cc.get_current_time()
            self.test_case_info.seconds_duration = cc.time_diff(self.test_case_info.start_time, self.test_case_info.end_time)
            chargeWithdrawBankCardPage.close_driver()

    def tearDown(self):
        self.test_report.write_html()

if __name__ == '__main__':
    unittest.main()


