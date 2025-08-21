from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
wd =webdriver.Edge()
wd.implicitly_wait(5)
wd.get('https://www.byhy.net/cdn2/files/selenium/sample2.html')
wd.switch_to.frame(wd.find_element(By.CSS_SELECTOR,'#frame1'))

elements =wd.find_elements(By.CSS_SELECTOR,'.plant')
for element in elements:
    print('====================')
    print(element.text)
    print(element.get_attribute('outerHTML'))

wd.switch_to.default_content()
wai_bu = wd.find_element(By.CSS_SELECTOR,'#outerbutton')
sleep(1)
wai_bu.click()
input('回车')
wd,quit()