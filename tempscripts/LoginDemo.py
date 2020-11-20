import pytest
from selenium import webdriver
import time

driver = webdriver.Chrome('../tools/chromedriver.exe')
url = "https://cas.leke.cn/login?service="
driver.get(url)
driver.maximize_window()
driver.find_element_by_id("loginName").send_keys('2525545')
driver.find_element_by_id("password").send_keys('leke1234')
driver.find_element_by_id("j-sign-on").click()
time.sleep(3)
driver.find_element_by_class_name("close--2npdy").click()
time.sleep(5)
driver.find_element_by_xpath("//*[@id='pageHome']/div/div[3]/div[1]/span/span/span").click()
