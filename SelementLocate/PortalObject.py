# -*- coding: utf-8 -*-
# Page element identifier页面元素
from selenium.webdriver.common.by import By

#登录页面
mobileInput = (By.ID, 'mobileInput')
pswInput = (By.ID, 'password')
loginButton = (By.ID, 'loginButton')
loginStatus = (By.XPATH, r'//div[@class="fr"]/ul/li[1]/a')
exitButton = (By.LINK_TEXT, '退出')

#注册页面
registerButton = (By.LINK_TEXT, '注册领礼包')
verifyCodeButton = (By.XPATH, r'//input[@value="获取验证码"]')
verifyCodeInput = (By.ID, 'mobileVerify')
registerConfirmButton = (By.ID, 'regButton')
errorMessage = (By.XPATH, r'//label[@class="onError error"]')

#我的账户页面
myAccountButton = (By.LINK_TEXT, '我的账户')
chargeButton = (By.LINK_TEXT, '充值')
withdrawButton = (By.LINK_TEXT, '提现')
moneyList = (By.XPATH, r'//ul[contains(@class,"user_property")]/li/span/font')
realnameButton = (By.LINK_TEXT, '立即认证')
#my account on the left panel
myAccountOnLeftPanelList = (By.XPATH, r'//ul[@class="my_side"]/li/a')

#实名认证页面
realnameInput = (By.ID, 'realName')
idCardInput = (By.ID, 'idCardInput')
realnameCertButton = (By.ID, 'realnameCertButton')

#绑卡页面
bankCardInput = (By.ID, 'bank_cardInput')
bankType = (By.ID, 'bank_type')
# outsideArea = (By.LINK_TEXT, '储蓄卡卡号：')
provinceSelect = (By.ID, 'province')
citySelect = (By.ID, 'city')
phoneNoInput = (By.ID, 'phone_no')
getValidCodeButInBindCard = (By.ID, 'get_valid_code')
validCodeInputInBindCard = (By.ID, 'valid_code')
bankCardSubmitBut = (By.ID, 'bankCardSubmitBtn')

#设置支付密码
setPayPswButton = (By.LINK_TEXT, '设置支付密码')
phoneInBankInput = (By.ID, 'tela')
getValidCodeButInSetPsw = (By.LINK_TEXT, '短信获取')
validCodeInputInSetPsw = (By.ID, 'J-sms')
setPswInputInSetPsw = (By.ID, 'J-psw')
setPswInputInSetPsw = (By.ID, 'J-check_psw')

# 充值页面
balanceInChargeWithdrawTab = (By.XPATH, r'//span[contains(text(),"可用余额：")]/../span[2]')
chargeInput = (By.ID, 'amount')
submitChargeButton = (By.LINK_TEXT, '立即充值')
onlinePayTab = (By.XPATH, r'//ul[@id="J-tabs"]/li[2]')
goPayOnlineButton = (By.XPATH, r'//form[@id="J-formOnline"]//button[@type="submit"]')
agreeButton = (By.ID, 'J-protocal')
attestationSuccessButton = (By.XPATH, r'//input[@value="验签成功"]')
paySuccessButton = (By.ID, 'J-paydone')
submitButton = (By.XPATH, r'//button[@type="submit"]')


# 提现页面
submitWithdrawButton = (By.LINK_TEXT, '确认提现')
submitWithdrawButton2 = (By.XPATH, r'//a[@class="pop_auto_log"]')
autoPop = (By.ID, 'pop_auto')
payPswInput = (By.ID, 'J-payPwdWITHDRAW')


#银行卡管理页面
unbindButton = (By.XPATH, r'//a[contains(@class,"unbind-card-btn")]')
withdrawButtonInPop = (By.LINK_TEXT, '立即提现')
bindCardButton = (By.XPATH, r'//img[@src="/images/light_style/addbankcard.jpg"]')