# -*- coding: utf-8 -*-

from BasePage import BasePage
from selenium.webdriver.common.by import By
from SelementLocate import BackManageObject
from ConstantLocate import Constant
import time


class BackManagePage(BasePage):

    # login
    def login(self):
        self.driver.find_element(*BackManageObject.mobileInput).send_keys(Constant.UserName)
        self.driver.find_element(*BackManageObject.passwordInput).send_keys(Constant.Password)
        self.find_element(*BackManageObject.loginButton).click()
        time.sleep(3)

    def create_rui_jin_product(self, name, rate, price, period, describe, base_title, base_content):
        self.find_element(*BackManageObject.namInput).send_keys(name)
        self.driver.find_elements(*BackManageObject.selectOptions).__getitem__(0)
        self.driver.find_elements(*BackManageObject.selectOptions).__getitem__(2)
        self.find_element(*BackManageObject.rateInput).send_keys(rate)
        self.find_element(*BackManageObject.priceInput).send_keys(price)
        self.find_element(*BackManageObject.lowInvestMoneyInput).send_keys(price)
        self.find_element(*BackManageObject.periodInput).send_keys(period)
        self.find_element(*BackManageObject.describeInput).send_keys(describe)
        self.find_element(*BackManageObject.titleInput).send_keys(base_title)
        self.find_element(*BackManageObject.contentInput).send_keys(base_content)
        self.find_element(*BackManageObject.saveButton).click()





