from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select

driver=webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver")

driver.get("https://www.oddsking.com")
driver.maximize_window()
driver.implicitly_wait(10)
#driver.get("https://www.browserstack.com")

driver.find_element_by_link_text("Join").click()
#join_form = driver.find_element_by_link_text('Join').click()

driver.find_element_by_id("RegistrationPage.AccountSection.email").send_keys('Olakunlejimoh@gmail.com')
driver.find_element_by_id("RegistrationPage.AccountSection.username").send_keys('Ola20212')
driver.find_element_by_id("RegistrationPage.AccountSection.password").send_keys('Secure01')
#driver.find_element_by_id("RegistrationPage.TermsAndConditions.agree_terms")
box = driver.find_element_by_class_name("_1yd4lz78").click()

driver.find_element_by_link_text("Continue").click()

# accept_cookies
# driver.find_element_by_css_selector('#page-wrapper > div._zdxht7 > div._12culun > div._1j7lbgv > div > div._1szrqxt > button')

checkbox = driver.find_element_by_class_name("_1yd4lz78")

Continue_button = driver.find_element_by_link_text("Continue")


