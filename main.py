import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from dotenv import load_dotenv
load_dotenv()

username = os.environ.get("USERNAME")
password = os.environ.get("PASSWORD")

year = "2022"
qtr = "1"
slns = ["17168", "17169"]
url = "https://sdb.admin.uw.edu/students/UWNetID/register.asp?INPUTFORM=UPDATE&PAC=0&MAXDROPS=0&_CW=7cc8256235328aa7d56bb7e40674a7de590e9f00e49490929a763146d096cf7f&_src=mp_reg_preview&QTR=" + qtr + "&YR=" + year

i = 1
for sln in slns:
    i_string = str(i)
    url += "&sln" + i_string + "=" + sln + "&entCode" + i_string + "=&credits" + i_string + "=&gr_sys" + i_string+ "="
    i += 1

browser = webdriver.Chrome()
browser.get(url)

browser.find_element_by_xpath('//*[@id="weblogin_netid"]').send_keys(username)
browser.find_element_by_xpath('//*[@id="weblogin_password"]').send_keys(password)
browser.find_element_by_xpath('//*[@id="weblogin_password"]').send_keys(Keys.ENTER)
