import selenium
print (selenium.__version__)
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()
browser.get("http://localoye.com/bangalore")
time.sleep(3)

inpot0= browser.find_elements_by_xpath("id('navbar')/x:ul/x:li[4]/x:a")
inpot0.click()

