from selenium import webdriver
from datetime import date
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
browser = webdriver.Firefox(executable_path="./drivers/geckodriver")
browser.get("https://intranet.primesoft.net/symfony/web/index.php/auth/login")
browser.find_element_by_id('txtUsername').send_keys(usr)
browser.find_element_by_id ('txtPassword').send_keys(pass)
browser.find_element_by_id("btnLogin").click()
browser.get("https://ams.primesoft.net/web/newWfhRequest")
browser.find_element_by_id('webapplicationbundle_ohrmuser_userName').send_keys(usr)
browser.find_element_by_id ('webapplicationbundle_ohrmuser_password').send_keys(pass)
browser.find_element_by_css_selector(".btn").click()

sleep(50)
sel = Select(browser.find_element_by_xpath("//select[@name='form[Sign_In_Time]']"))
sel.select_by_visible_text("14:00")
sel1 = Select(browser.find_element_by_xpath("//select[@name='form[Sign_Out_Time]']"))
sel1.select_by_visible_text("23:00")
browser.find_element_by_id('form_Comments').send_keys("S4 Shift")
browser.find_element_by_id('submitBtn').click()
