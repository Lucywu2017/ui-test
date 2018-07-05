# -*- coding: utf-8 -*-
# @Time    : 2017-11-21 13:35
# @Author  : 伍露露
# 测试注册、实名认证、绑卡、设置支付密码功能

import unittest
import CommonLibrary.CommonConfiguration as cc
from CommonLibrary.LogUtility import LogUtility
from CommonLibrary.TestReport import TestReport
from CommonLibrary.TestCaseInfo import TestCaseInfo
from WebPages.CertificationPage import NewUserCertificationPage
from ConstantLocate import Constant
import random
from time import sleep
from CommonLibrary.Util import getsmscode, clear_logcat, get_id_card
from CommonLibrary.modern import session, Users, UsersInfo


class TestRegisterRealNameBindCardSetPassword(unittest.TestCase):

    def setUp(self):
        self.test_case_info = TestCaseInfo(id=1, name="Test New User Certificate", author='Automation', result='Failed', start_time=cc.get_current_time())
        self.test_report = TestReport(self.test_case_info)
        self.logger = LogUtility()
        self.logger.create_logger_file('Test_New_User_Certificate')

    def test_registerRealNameBindCardSetPassword(self):

        '''
            注册前操作步骤:
                1.查询测试用户[mobile]是否存在[wb_users表]
                2.查询测试用户[user_id]信息是否存在[wb_users_info表]
                3.删除测试用户信息[wb_users_info表]
                4.删除测试用户[wb_users表]
         '''
        # Step1: 注册
        queryUsers = session.query(Users)
        users = queryUsers.filter(Users.mobile == Constant.NewUser).scalar()
        if users is not None:
            queryUsersInfo = session.query(UsersInfo)
            usersInfo = queryUsersInfo.filter(UsersInfo.user_id == users.id).scalar()
            if usersInfo is not None:
                session.delete(usersInfo)
                session.flush()
            session.delete(users)
            session.flush()
            session.commit()
        else:
            print('开始注册......')
        newUserCertificationPage = NewUserCertificationPage()
        newUserCertificationPage.open(Constant.RegisterURL)
        newUserCertificationPage.new_user_register(Constant.NewUser, Constant.Password)
        print('注册中......')
        #check point: 注册成功后的链接正确
        self.assertTrue(newUserCertificationPage.get_current_url().__contains__("realname-auth/1"))
        print('注册完成......')
        #进到我的账户页面去实名认证
        newUserCertificationPage.click_my_account()

        # Step2: 实名认证
        print('开始实名认证......')
        newUserCertificationPage.click_realname_button()
        newUserCertificationPage.enter_realname(Constant.Realname)
        idCard = get_id_card()
        newUserCertificationPage.enter_id_card(idCard)
        newUserCertificationPage.click_realname_cert_button()
        print('实名认证完成......')

        #Step3: 绑卡
        print('开始绑定银行卡......')
        # 填写储蓄卡卡号
        bankCardNum = Constant.CardNumber + str(random.randint(10000000000000, 99999999999999))
        newUserCertificationPage.enter_bank_card(bankCardNum)
        newUserCertificationPage.click_outside()
        self.assertTrue(newUserCertificationPage.get_bank_type() == "中国邮储银行")
        newUserCertificationPage.select_province(Constant.Province)
        newUserCertificationPage.select_city(Constant.City)
        newUserCertificationPage.enter_phone_bank(Constant.MobileInBank)
        #获取验证码并填写
        clear_logcat()
        newUserCertificationPage.click_get_valid_code_in_bind_card()
        smsCode = getsmscode()
        newUserCertificationPage.enter_valid_code_in_bind_card(smsCode)
        newUserCertificationPage.click_bank_card_submit_button()
        print('绑定银行卡完成......')

        # Step4: 设置支付密码
        print('开始设置支付密码......')
        newUserCertificationPage.click_set_pay_password_button()
        newUserCertificationPage.enter_phone_in_bank(Constant.MobileInBank)
        newUserCertificationPage.click_get_valid_code_in_set_psw()
        smsCode = getsmscode()
        newUserCertificationPage.enter_valid_code_in_set_psw(smsCode)
        newUserCertificationPage.enter_pay_psw_in_set_psw(Constant.Password)
        newUserCertificationPage.enter_pay_psw_again_in_set_psw(Constant.Password)
        newUserCertificationPage.click_submit_button()
        print('设置支付交易密码成功......')


        try:
            # All case is passed
            self.test_case_info.result = "Pass"


        except Exception as err:
            self.test_case_info.error_info = str(err)
            self.logger.log(("Got error: "+str(err)))
        finally:
            self.test_case_info.end_time = cc.get_current_time()
            self.test_case_info.seconds_duration = cc.time_diff(self.test_case_info.start_time, self.test_case_info.end_time)
            newUserCertificationPage.close_driver()
        pass

    def tearDown(self):
        self.test_report.write_html()

if __name__ == '__main__':
    unittest.main()



