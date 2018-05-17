# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By

# Page element identifier
#Background management page
loginNameInput = (By.ID, 'loginName')
passwordInput = (By.ID, 'password')
loginButton = (By.ID, 'loginButton')

#添加产品
namInput = (By.XPATH, '//input[@value="睿进1期"]')
selectOptions = (By.XPATH, '//select/option')
rateInput = (By.XPATH, '//input[@name="p_HistoryRate"]')
priceInput = (By.XPATH, '//input[@name="price"]')
lowInvestMoneyInput = (By.XPATH, '//input[@name="p_LowInvestableMoney"]')
periodInput = (By.XPATH, '//input[@name="p_Period"]')
describeInput = (By.XPATH, '//textarea[@name="p_describe"]')
titleInput = (By.XPATH, '//input[@name="base_info_title[]"]')
contentInput = (By.XPATH, '//textarea[@name="base_info_content[]"]')
saveButton = (By.ID, 'saveButton')
