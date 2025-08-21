
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

wd =webdriver.Edge()
wd.get('https://www.byhy.net/cdn2/files/selenium/test4.html')
wd.find_element(By.ID,'b1').click()
print(wd.switch_to.alert.text)
sleep(1)
wd.switch_to.alert.accept()
sleep(1)
wd.find_element(By.ID,'b2').click()
sleep(1)
print(wd.switch_to.alert.text)
wd.switch_to.alert.accept()
sleep(1)
wd.find_element(By.CSS_SELECTOR,'#b2').click()
sleep(1)
wd.switch_to.alert.dismiss()
sleep(1)
wd.find_element(By.CSS_SELECTOR,'#b3').click()
sleep(1)
alert =wd.switch_to.alert
print(alert.text)
text = 'selenium自动化'
alert.send_keys(text)
print(f'我的选择是：{text}')
sleep(3)
alert.accept()
sleep(1)
wd.find_element(By.CSS_SELECTOR,'#b3').click()
sleep(1)
alert.dismiss()
input()