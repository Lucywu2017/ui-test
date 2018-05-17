# -*- coding: utf-8 -*-
# @Time    : 2017-12-22 13:22
# Function/CreateRuiJinProduct.py
# 后台管理相关的业务功能脚本（用例脚本可调用此处的功能脚本）

from WebPages.BackManagePage import BackManagePage as backManage

from selenium import webdriver
import unittest
import CommonLibrary.CommonConfiguration as cc
from CommonLibrary.LogUtility import LogUtility
from CommonLibrary.TestReport import TestReport
from CommonLibrary.TestCaseInfo import TestCaseInfo
from datetime import datetime
from WebPages.BackManagePage import BackManagePage
from ConstantLocate import Constant
import time

current = time.strftime('%yy%mm%dd', time.localtime(time.time()))
sixPeriodName = "铂诺睿进6月期"+time.strftime('%yy%mm%dd', time.localtime(time.time()))
twelvePeriodName = "铂诺睿进12月期"+time.strftime('%yy%mm%dd', time.localtime(time.time()))
print(current)

# 打开后台管理，添加6、12月期的创新型睿进产品
class Function(unittest.TestCase):

    def setUp(self):
        self.baseURL = Constant.CreateRuiJinProductURL

    def create_rui_jin_product(self):
        # Step1: open base site and login
        backManage = BackManagePage()
        backManage.open(self.baseURL)
        backManage.login()

        # Step2: create 6 and 12 mouths ruijin product
        backManage.create_rui_jin_product(self, name, rate, price, period, describe, base_title, base_content)




    def tearDown(self):
        backManage.closeDriver()

if __name__ == '__main__':
    unittest.main()