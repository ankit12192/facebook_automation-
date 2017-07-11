import selenium
print (selenium.__version__)
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()
browser.get("https://inet.idbibank.co.in/corp/BANKAWAY?Action.RetUser.Init.001=Y&AppSignonBankId=IBKL&AppType=corporate")

inputElement = browser.find_element_by_name('CorporateSignonCorpId')
inputElement2 = browser.find_element_by_name('CorporateSignonPassword')
#browser.find_elements_by_name("fldLoginUserId")

inputElement.send_keys('id')
inputElement2.send_keys('pass')
inputElement.send_keys(Keys.ENTER)
time.sleep(2)

in3= browser.find_element_by_name("Action.Go")
in3.click()

in4 = browser.find_element_by_link_text("Accounts")
in4.click()

