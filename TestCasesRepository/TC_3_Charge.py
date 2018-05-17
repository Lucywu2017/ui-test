# -*- coding: utf-8 -*-
# @Time    : 2017-12-25 14:22
# @Author  : 伍露露
# 充值功能测试

import unittest
import CommonLibrary.CommonConfiguration as cc
from CommonLibrary.LogUtility import LogUtility
from CommonLibrary.TestReport import TestReport
from CommonLibrary.TestCaseInfo import TestCaseInfo
from WebPages.ChargeWithdrawBankCardPage import ChargeAndWithdrawBankCardPage
from ConstantLocate import Constant


class TestCharge(unittest.TestCase):

    def setUp(self):
        self.test_case_info = TestCaseInfo(id=3, name="Test Charge", author='Automation', result='Failed', start_time=cc.get_current_time())
        self.test_report = TestReport(self.test_case_info)
        self.logger = LogUtility()
        self.logger.create_logger_file('Test_Charge')

    def test_charge(self):
        try:
            # Step1: 登录
            chargeAndWithdrawBankCardPage = ChargeAndWithdrawBankCardPage()
            chargeAndWithdrawBankCardPage.open(Constant.LoginURL)
            chargeAndWithdrawBankCardPage.login(Constant.UserName, Constant.Password)

            # Step2: 充值前去我的账户页面查看可用余额
            chargeAndWithdrawBankCardPage.click_my_account_on_left_panel()
            balanceInAccount = chargeAndWithdrawBankCardPage.get_balance_in_account()

            # Step3: 充值 - 网银
            chargeAndWithdrawBankCardPage.click_charge_in_account()
            chargeAndWithdrawBankCardPage.send_charge_withdraw_amount(1800)
            chargeAndWithdrawBankCardPage.click_submit_charge()
            chargeAndWithdrawBankCardPage.click_online_pay_button()
            chargeAndWithdrawBankCardPage.click_go_pay_online()
            chargeAndWithdrawBankCardPage.close_driver()
            chargeAndWithdrawBankCardPage.switch_to_window('Insert')
            chargeAndWithdrawBankCardPage.click_attestation_success()
            chargeAndWithdrawBankCardPage.accept_alert()

            # Step4: 充值后去我的账户页面查看可用余额
            chargeAndWithdrawBankCardPage.click_my_account_on_left_panel()
            currentBalanceInAccount = chargeAndWithdrawBankCardPage.get_balance_in_account()

            #校验充值前后的可用余额
            self.assertEqual(balanceInAccount.__add__(1800.00), currentBalanceInAccount)

            # All case is passed
            self.test_case_info.result = "Pass"

        except Exception as err:
            self.test_case_info.error_info = str(err)
            self.logger.log(("Got error: "+str(err)))
        finally:
            self.test_case_info.end_time = cc.get_current_time()
            self.test_case_info.seconds_duration = cc.time_diff(self.test_case_info.start_time, self.test_case_info.end_time)
            chargeAndWithdrawBankCardPage.close_driver()

    def tearDown(self):
        self.test_report.write_html()

if __name__ == '__main__':
    unittest.main()


