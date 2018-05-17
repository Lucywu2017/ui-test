# -*- coding: utf-8 -*-
# @Time    : 2018-01-18 13:35
# @Author  : 伍露露
# 提现功能测试

import unittest
import CommonLibrary.CommonConfiguration as cc
from CommonLibrary.LogUtility import LogUtility
from CommonLibrary.TestReport import TestReport
from CommonLibrary.TestCaseInfo import TestCaseInfo
from WebPages.ChargeWithdrawBankCardPage import ChargeAndWithdrawBankCardPage
from ConstantLocate import Constant


class TestWithdraw(unittest.TestCase):

    def setUp(self):
        self.test_case_info = TestCaseInfo(id=4, name="Test Withdraw", author='Automation', result='Failed', start_time=cc.get_current_time())
        self.test_report = TestReport(self.test_case_info)
        self.logger = LogUtility()
        self.logger.create_logger_file('Test_Withdraw')

    def test_withdraw(self):
        try:
            # Step1: 登录
            chargeWithdrawBankCardPage = ChargeAndWithdrawBankCardPage()
            chargeWithdrawBankCardPage.open(Constant.LoginURL)
            chargeWithdrawBankCardPage.login(Constant.UserName, Constant.Password)

            # Step2: 提现前去我的账户页面查看可用余额
            chargeWithdrawBankCardPage.click_my_account_on_left_panel()
            balanceInAccount = chargeWithdrawBankCardPage.get_balance_in_account()

            # Step3: 提现
            chargeWithdrawBankCardPage.click_withdraw_in_account()
            chargeWithdrawBankCardPage.send_charge_withdraw_amount(100)
            chargeWithdrawBankCardPage.click_submit_withdraw()
            #测试点：温馨提示弹框出现
            self.assertTrue(chargeWithdrawBankCardPage.is_auto_pop_show())
            chargeWithdrawBankCardPage.click_submit_withdraw()
            chargeWithdrawBankCardPage.enter_pay_password_in_withdraw(Constant.Password)
            chargeWithdrawBankCardPage.click_success_withdraw_button()

            # Step4: 提现后去我的账户页面查看可用余额
            chargeWithdrawBankCardPage.click_my_account_on_left_panel()
            currentBalanceInAccount = chargeWithdrawBankCardPage.get_balance_in_account()

            #校验提现前后的可用余额
            self.assertEqual(balanceInAccount.__add__(-100.00), currentBalanceInAccount)

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


