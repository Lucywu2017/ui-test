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

from TestCasesRepository import TC_1_NewUserCertificate, TC_2_Login, TC_3_Charge, TC_4_Withdraw, TC_6_UnbindCard, TC_7_BindCard
def suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(TC_2_Login.TestLogin('test_login.py'))
    # test_suite.addTest(TC_3_Charge.TestCharge('test_charge.py'))
    # test_suite.addTest(TC_4_Withdraw.TestWithdraw('test_withdraw.py'))
    return test_suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())
