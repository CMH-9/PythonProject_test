#radio框
'''from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep



wd = webdriver.Edge()
wd.implicitly_wait(5)
wd.get("https://www.byhy.net/cdn2/files/selenium/test2.html")
element =wd.find_element(By.CSS_SELECTOR,'#s_radio [name=teacher][checked]')
print(element.get_attribute('value'))
print(element.get_attribute('outerHTML'))
sleep(1)

wd.find_element(By.CSS_SELECTOR,'#s_radio [value=小江老师]').click()
sleep(1)
element =wd.find_element(By.CSS_SELECTOR,'#s_radio [name=teacher]:checked')
print(element.get_attribute('value'))
print(element.get_attribute('outerHTML'))'''
#checkbox框
'''from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


wd = webdriver.Edge()
wd.implicitly_wait(5)
wd.get("https://www.byhy.net/cdn2/files/selenium/test2.html")
sleep(2)
element =wd.find_element(By.CSS_SELECTOR,'[name=teachers1][checked]')
element.click()

sleep(1)

wd.find_element(By.CSS_SELECTOR,'[name=teachers1][value=小江老师]').click()
sleep(1)
element =wd.find_elements(By.CSS_SELECTOR,'#s_checkbox [name=teachers1]:checked')

print(element[0].get_attribute('value'))#----0
wd.find_element(By.CSS_SELECTOR,'[name=teachers1][value=小凯老师]').click()
sleep(1)
element =wd.find_elements(By.CSS_SELECTOR,'#s_checkbox [name=teachers1]:checked')
print(element[-1].get_attribute('value'))#---1
wd.find_element(By.CSS_SELECTOR,'[name=teachers1][value=小雷老师]').click()
sleep(1)
element =wd.find_elements(By.CSS_SELECTOR,'#s_checkbox [name=teachers1]:checked')
print(element[-2].get_attribute('value'))
element =wd.find_element(By.CSS_SELECTOR,'[name=teachers1][checked]')
element.click()
sleep(1)

wd.find_element(By.CSS_SELECTOR,'[name=teachers1][value=小凯老师]').click()
element =wd.find_elements(By.CSS_SELECTOR,'#s_checkbox [name=teachers1]:checked')
print(element[-3].get_attribute('value'))
input()'''
#select框
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from time import sleep

wd = webdriver.Edge()
wd.implicitly_wait(5)
wd.get("https://www.byhy.net/cdn2/files/selenium/test2.html")

# 首先获取默认选中的选项
element = wd.find_element(By.CSS_SELECTOR, '#ss_single option:selected')
print("默认选中的值:", element.get_attribute('value'))
print("默认选中的outerHTML:", element.get_attribute('outerHTML'))

sleep(1)

# 使用Select类选择小江老师
select = Select(wd.find_element(By.ID, "ss_single"))
select.select_by_visible_text("小江老师")

sleep(1)

# 再次获取当前选中的选项
element = wd.find_element(By.CSS_SELECTOR, '#ss_single option:selected')
print("选择后选中的值:", element.get_attribute('value'))
print("选择后选中的outerHTML:", element.get_attribute('outerHTML'))

sleep(1)

wd.quit()
