# -*- coding: utf-8 -*-
# @Time    : 2017-11-21 13:35
# @Author  : 伍露露
# 公共的方法类

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from SelementLocate import PortalObject
import math


class BasePage(object):
    """default driver: firefox"""

    def __init__(self, browser='firefox'):
        '''
        initialize selenium webdriver, use chrome as default webdriver
        '''

        if browser == "firefox" or browser == "ff":
            driver = webdriver.Firefox(executable_path="..\\geckodriver.exe", log_path="..\\geckodriver.log")
            driver.maximize_window()
        elif browser == "chrome":
            driver = webdriver.Chrome()
        elif browser == "internet explorer" or browser == "ie":
            driver = webdriver.Ie()
        elif browser == "opera":
            driver = webdriver.Opera()
        elif browser == "phantomjs":
            driver = webdriver.PhantomJS()
        try:
            self.driver = driver
        except Exception:
            raise NameError("Not found %s browser,You can enter 'ie', 'ff' or 'chrome'." % browser)

    def open(self, url):
        '''
        Open web url

        Usage:
        self.open(url)
        '''
        if url != "":
            self.driver.get(url)
        else:
            raise ValueError("please provide a base url")
        time.sleep(3)

    def quit(self):
        '''
        Quit webdriver
        '''
        self.driver.quit()

    def get_title(self):
        '''
        Get window title
        '''
        return self.driver.title

    def get_current_url(self):
        '''
        Get current url
        '''
        return self.driver.current_url

    def get_screen_shot(self, target_path):
        '''
        Get current screenshot and save it to target path
        '''
        self.driver.get_screenshot_as_file(target_path)

    def maximize_window(self):
        """
        Maximize current browser window
        """
        self.driver.maximize_window()

    def back(self):
        """
        Goes one step backward in the browser history.
        """
        self.driver.back()

    def forward(self):
        """
        Goes one step forward in the browser history.
        """
        self.driver.forward()

    def get_window_size(self):
        """
        Gets the width and height of the current window.
        """
        return self.driver.get_window_size()

    def refresh(self):
        """
        Refresh current page
        """
        self.driver.refresh()

    def close_driver(self):
        """
        close Driver
        """
        self.driver.close()
        time.sleep(2)

    def switch_to_window(self, window_title):
        """
        switch to the number of window
        :param window_title: 
        """

        try:
            all_handles = self.driver.window_handles  # 获取所有windowhandle
            for handle in all_handles:
                self.driver.switch_to.window(handle)
                print('Current url:' + self.driver.current_url)
                # 判断title是否和handles当前的窗口相同
                if self.driver.title.__contains__(window_title):
                    print('Switch to window: ' + window_title + ' successfully!')
                    return True
                    break
                else:
                    continue
        except Exception:
            print('Window: ' + window_title + ' could not found!')
            return False

        time.sleep(2)

    def accept_alert(self):
        """
         accept the current window alert
        """
        self.driver.switch_to.alert.accept()
        time.sleep(3)


    #登录tab
    def input_username(self, user_input):
        """
        输入手机号
        :param user_input: 
        """
        self.driver.find_element(*PortalObject.mobileInput).send_keys(user_input)

    def input_password(self, pwd_input):
        """
        输入登录密码
        :param pwd_input: 
        :return: 
        """
        self.driver.find_element(*PortalObject.pswInput).send_keys(pwd_input)

    def click_sign_in(self):
        """点击登录按钮"""
        self.driver.find_element(*PortalObject.loginButton).click()

    def get_login_status(self):
        """获取登录状态"""
        status = self.driver.find_element(*PortalObject.loginStatus).text
        return status

    def click_exit(self):
        """
        点击退出
        """
        self.driver.find_element(*PortalObject.exitButton).click()

    def login(self, username, password):
        """
        登录
        :param username: 
        :param password: 
        :return: 
        """
        self.input_username(username)
        self.input_password(password)
        self.click_sign_in()
        time.sleep(3)


    #点击我的账户按钮
    def click_my_account(self):
        """
        点击进到我的账户页面
        """
        self.driver.find_element(*PortalObject.myAccountButton).click()
        time.sleep(3)

    def click_charge_in_account(self):
        """
        点击我的账户页面的充值按钮
        """
        self.driver.find_element(*PortalObject.chargeButton).click()

    def click_withdraw_in_account(self):
        """
        点击我的账户页面的提现按钮
        """
        self.driver.find_element(*PortalObject.withdrawButton).click()

    def get_total_account_assets(self):
        """
        获取账户总资产
        :return: 
        """
        balance = self.driver.find_element(*PortalObject.loginStatus).text
        print('账户总资产：' + balance)
        return balance

    def get_balance_in_account(self):
        """
        获取可用余额
        :return: 
        """
        value = self.driver.find_elements(*PortalObject.moneyList).__getitem__(1).text
        balance = float(value.strip()[:-1].replace(',', ''))
        print("可用余额：" + str(balance))
        return balance

    #我的账户tab
    def click_my_account_on_left_panel(self):
        """
        点击进到我的账户页面
        """
        self.driver.find_elements(*PortalObject.myAccountOnLeftPanelList).__getitem__(0).click()
        time.sleep(3)

    # 银行卡管理tab
    def click_bank_card_manage_on_left_panel(self):
        """
        点击左边的银行卡管理tab
        """
        self.driver.find_elements(*PortalObject.myAccountOnLeftPanelList).__getitem__(4).click()
        time.sleep(3)

    def click_add_bank_card(self):
        """
        点击添加银行卡
        """
        self.driver.find_element(*PortalObject.bindCardButton).click()
        time.sleep(3)


    #充值提现tab
    def click_charge_withdraw_on_left_panel(self):
        """
        点击左边的充值提现tab
        """
        self.find_elements(*PortalObject.myAccountOnLeftPanelList).__getitem__(5).click()
        time.sleep(2)






