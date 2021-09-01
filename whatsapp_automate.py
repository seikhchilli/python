from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
browser = webdriver.Chrome('C:/Users/saura/Downloads/chromedriver_win32/chromedriver')
browser.get('https://web.whatsapp.com/')
wait = WebDriverWait(browser, 600)
target = '"Suman"' #enter contact name here
string = "...." #target msg
x_arg = ' //span[contains(@title, ' + target +')]'
target = wait.until(ec.presence_of_element_located((By.XPATH, x_arg)))
target.click()



inp_xpath = '//div[@class="_13NKt copyable-text selectable-text"][@dir="ltr"][@data-tab="6"]'
input_box = wait.until(ec.presence_of_element_located((By.XPATH, inp_xpath)))
for i in range(100):
    input_box.send_keys(string + Keys.ENTER)
    time.sleep(1)