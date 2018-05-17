# -*- coding: utf-8 -*-
# @Time    : 2017-11-21 13:35
# @Author  : 伍露露
# 测试充值功能

import unittest
import CommonLibrary.CommonConfiguration as cc
from CommonLibrary.LogUtility import LogUtility
from CommonLibrary.TestReport import TestReport
from CommonLibrary.TestCaseInfo import TestCaseInfo
from WebPages.BasePage import BasePage
from ConstantLocate import Constant


class TestLogin(unittest.TestCase):

    def setUp(self):
        self.test_case_info = TestCaseInfo(id=2, name="Test Login", author='Automation', result='Failed', start_time=cc.get_current_time())
        self.test_report = TestReport(self.test_case_info)
        self.logger = LogUtility()
        self.logger.create_logger_file('Test_Login')

    def test_login(self):
        try:
            #Step1: open base site
            basePage = BasePage()
            basePage.open(Constant.LoginURL)

            # Step2: Enter username & password
            basePage.login(Constant.UserName, Constant.Password)

            # Checkpoint1: Check login frame title
            text = basePage.get_login_status()
            self.assertTrue(text, "我的账户")

            # All case is passed
            self.test_case_info.result = "Pass"

        except Exception as err:
            self.test_case_info.error_info = str(err)
            self.logger.log(("Got error: "+str(err)))
        finally:
            self.test_case_info.end_time = cc.get_current_time()
            self.test_case_info.seconds_duration = cc.time_diff(self.test_case_info.start_time, self.test_case_info.end_time)
            basePage.close_driver()

    def tearDown(self):
        self.test_report.write_html()

if __name__ == '__main__':
    unittest.main()


