# -*- coding: utf-8 -*-
# @Time    : 2017-05-10 16:34
# all_case.py

import unittest
import HTMLTestRunner
import time,os,datetime


# 取test_case文件夹下所有用例文件
def creatsuitel(lists):
    testunit = unittest.TestSuite()
    # discover 方法定义
    discover = unittest.defaultTestLoader.discover(lists, pattern='TC_*.py', top_level_dir=None)
    #discover 方法筛选出来的用例，循环添加到测试套件中
    for test_suite in discover:
        for test_case in test_suite:
            testunit.addTests(test_case)
            print(testunit)
    return testunit
list_1 = 'TestCasesRepository'
alltestnames = creatsuitel(list_1)

#取前面时间加入到测试报告文件名中
now = time.strftime("%Y-%m-%d", time.localtime(time.time()))
filename = "TestResult\\"+now+'result.html' #定义个报告存放路径，支持相对路径。
fp = open(filename, 'wb')
runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'自动化测试报告', description=u'用例执行情况')

if __name__ == "__main__":
    # 执行测试用例集并生成报告
    runner = unittest.TextTestRunner()