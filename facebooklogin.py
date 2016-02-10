__author__ = 'Ankit'

import getpass
import selenium
print (selenium.__version__)
import time
start_time = time.time()
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
browser = webdriver.Firefox()
browser.get("https://www.facebook.com/?stype=lo&jlou=AfcQ_86A5ZptlNVbtzPICyBj67QzLyd9gw-mUVLxY3F716_HD8wBHd-SuRBxnS3V2l9lZ0J2pzQxn_5TPw-yGOHyi8SpYNyKTRCssjqrb0jrAw&smuh=29247&lh=Ac9E7omSe5g2BsR_")
inputElement = browser.find_element_by_name('email')
phone =raw_input("Enter Phone number or email")
inputElement2 = browser.find_element_by_name('pass')
password = getpass.getpass()
inputElement.send_keys(phone)
inputElement2.send_keys(password)
inputElement.send_keys(Keys.ENTER)
print("Logged in ")
print("total --- %s seconds --- taken to login " % (time.time() - start_time))
