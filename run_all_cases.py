# coding:utf-8
import unittest
import os
# # 用例路径
# case_path = os.path.join(os.getcwd(), "TestCasesRepository")
# # 报告存放路径
# report_path = os.path.join(os.getcwd(), "report")
# def all_case():
#     discover = unittest.defaultTestLoader.discover(case_path, pattern="TC_*.py", top_level_dir=None)
#     print(discover)
#     return discover

from TestCasesRepository import TestRegisterRealNameBindCardSetPassword
def suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(TestRegisterRealNameBindCardSetPassword('test_registerRealNameBindCardSetPassword.py'))
    test_suite.addTest(TestLogin('test_login.py'))
    test_suite.addTest(TestCharge('test_charge.py'))
    test_suite.addTest(TestWithdraw('test_withdraw.py'))
    return test_suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())
