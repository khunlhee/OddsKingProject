from telnetlib import EC

import until as until
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
import time

driver=webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver")

driver.get("https://www.oddsking.com/lotto/irish")
driver.maximize_window()
driver.implicitly_wait(10)


#driver.find_element_by_link_text("Results").click()
Results_link = driver.find_element_by_css_selector("#page-inner-content > div > div > div._1zz89h > div:nth-child(1) > div > div._7fhkux > div._1h22rc2 > a").click()
#driver.find_element("_1h22rc2")
#Results_link=driver.find_element_by_id("_1thjhe2 marked-element-temp").click()

#result filter
date_dropdown = driver.find_element_by_id("_2fdesk").click()

#Select navigation arrow
driver.find_element_by_id("_pozy24")
