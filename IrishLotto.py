import until as until
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver=webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver")

driver.get("https://techwithtim.net/")

link = driver.find_element_by_link_text("Python Programming")
link.ckick()


