
"""
This Script can be used to wish Happpy Birthday by just using python command line
prerequisite : The following libraries should be installed

1. urllib
2. getpass
3. selenium
4. requests

step to run
python facebooklogin.py
"""

#---------------------------
#	Importing Modules
#---------------------------

__author__ = 'Ankit'
import  requests
import requests.exceptions
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from requests.exceptions import ConnectionError
import getpass
import time

#Will be converting into modules
browser = webdriver.Firefox()
browser.get("https://www.facebook.com/?stype=lo&jlou=AfcQ_86A5ZptlNVbtzPICyBj67QzLyd9gw-mUVLxY3F716_HD8wBHd-SuRBxnS3V2l9lZ0J2pzQxn_5TPw-yGOHyi8SpYNyKTRCssjqrb0jrAw&smuh=29247&lh=Ac9E7omSe5g2BsR_")
def login():

    try:
        m=requests.get("https://www.facebook.com/?stype=lo&jlou=AfcQ_86A5ZptlNVbtzPICyBj67QzLyd9gw-mUVLxY3F716_HD8wBHd-SuRBxnS3V2l9lZ0J2pzQxn_5TPw-yGOHyi8SpYNyKTRCssjqrb0jrAw&smuh=29247&lh=Ac9E7omSe5g2BsR_")
    except Exception as  e:
        print("No net connection ")
        exit()
    #browser.get("https://www.facebook.com/?stype=lo&jlou=AfcQ_86A5ZptlNVbtzPICyBj67QzLyd9gw-mUVLxY3F716_HD8wBHd-SuRBxnS3V2l9lZ0J2pzQxn_5TPw-yGOHyi8SpYNyKTRCssjqrb0jrAw&smuh=29247&lh=Ac9E7omSe5g2BsR_")
    inputElement = browser.find_element_by_name('email')
    phone =raw_input("Enter Phone number or email - > ")
    inputElement2 = browser.find_element_by_name('pass')
    password = getpass.getpass()
    inputElement.send_keys(phone)
    inputElement2.send_keys(password)
    inputElement.send_keys(Keys.ENTER)
    start_time = time.time()
    try:
        browser.find_element_by_tag_name('textarea').is_displayed()
        print("Logged in !")
        print("total --- %s seconds --- taken to login " % (int(time.time() - start_time)*100))
    except Exception as e:
        print("Can Not login check email/phone or password !")
        exit(0)

def Happy_birthday():

    try:
        en09=browser.find_element_by_xpath('//*[@id="pagelet_reminders"]/div/div/div[2]/div/a/div/div/span/span')
        #dddddd

        if en09!=0:

            if en09.is_displayed():
                msg=raw_input("Enter Birthday message - > ")
                en09.click()
                time.sleep(3)
                en10=browser.find_element_by_name('message_text')
                en10.send_keys(msg)
            else:
                print("NO Element found")
        else:
            print("Tag not found ")
    except:
        print("Can Not find any birthday")

def logout():

    try:
        lsb=browser.find_element_by_xpath('//*[@id="pageLoginAnchor"]')
        lsb.click()
        time.sleep(5)
        mlb=browser.find_element_by_xpath('//*[@id="u_d_3"]/div/div/div[1]/div/div/ul/li[16]')
        time.sleep(2)
        mlb.click()
        inputElement33 = browser.find_element_by_name('pass').is_displayed()
        print("Looged out")
    except:
        print("Cannot logout")
        
# Running modules
login()
Happy_birthday()
logout()
