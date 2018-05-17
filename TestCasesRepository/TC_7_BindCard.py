# -*- coding: utf-8 -*-
# @Time    : 2018-01-19 15:20
# @Author  : 伍露露
# 绑卡功能测试

import unittest
import CommonLibrary.CommonConfiguration as cc
from CommonLibrary.LogUtility import LogUtility
from CommonLibrary.TestReport import TestReport
from CommonLibrary.TestCaseInfo import TestCaseInfo
from WebPages.ChargeWithdrawBankCardPage import ChargeAndWithdrawBankCardPage
from CommonLibrary.Util import getsmscode, clear_logcat
from ConstantLocate import Constant
import random


class TestBindCard(unittest.TestCase):

    def setUp(self):
        self.test_case_info = TestCaseInfo(id=7, name="Test Bind", author='Automation', result='Failed', start_time=cc.get_current_time())
        self.test_report = TestReport(self.test_case_info)
        self.logger = LogUtility()
        self.logger.create_logger_file('Test_Bind')

    def test_bind_card(self):
        try:
            # Step1: 登录
            chargeAndWithdrawBankCardPage = ChargeAndWithdrawBankCardPage()
            chargeAndWithdrawBankCardPage.open(Constant.LoginURL)
            chargeAndWithdrawBankCardPage.login(Constant.NewUser, Constant.Password)

            # Step2:在银行卡管理页面绑卡
            chargeAndWithdrawBankCardPage.click_my_account()
            chargeAndWithdrawBankCardPage.click_bank_card_manage_on_left_panel()
            # chargeAndWithdrawBankCardPage.click_add_bank_card()
            print('开始绑定银行卡......')
            # 填写储蓄卡卡号
            bankCardNum = Constant.CardNumber + str(random.randint(10000000000000, 99999999999999))
            chargeAndWithdrawBankCardPage.enter_bank_card(bankCardNum)
            chargeAndWithdrawBankCardPage.click_outside()
            self.assertTrue(chargeAndWithdrawBankCardPage.get_bank_type() == "中国邮储银行")
            chargeAndWithdrawBankCardPage.select_province(Constant.Province)
            chargeAndWithdrawBankCardPage.select_city(Constant.City)
            chargeAndWithdrawBankCardPage.enter_phone_bank(Constant.MobileInBank)
            # 获取验证码并填写
            clear_logcat()
            chargeAndWithdrawBankCardPage.click_get_valid_code_in_bind_card()
            smsCode = getsmscode()
            chargeAndWithdrawBankCardPage.enter_valid_code_in_bind_card(smsCode)
            chargeAndWithdrawBankCardPage.click_bank_card_submit_button()
            self.assertTrue(chargeAndWithdrawBankCardPage.get_current_url().__contains__("bind-success"))
            print('绑定银行卡完成......')

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


