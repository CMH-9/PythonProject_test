'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

cmh =webdriver.Edge()
cmh.implicitly_wait(5)
cmh.get('https://www.bilibili.com/')
shu_ru =cmh.find_element(By.CSS_SELECTOR,'.nav-search-input')
shu_ru.click()
shu_ru.send_keys("二棉裤说剧")

sou_suo = cmh.find_element(By.CSS_SELECTOR,'.nav-search-btn')
sou_suo.click()

video_card = cmh.find_element(By.CSS_SELECTOR, '.bili-video-card:first-child .bili-video-card__wrap')
video_card.click()

shi_pin = cmh.find_element(By.CSS_SELECTOR,'.bili-video-card:first-child img')
shi_pin.click()

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import element_to_be_selected

# 加上参数，禁止 chromedriver 日志写屏
options = webdriver.EdgeOptions()
options.add_experimental_option(
    'excludeSwitches', ['enable-logging'])

#创建webdriver对象
wd = webdriver.Edge(options=options)

wd.get('https://www.byhy.net/cdn2/files/selenium/stock1.html')
element =wd.find_elements(By.TAG_NAME,'nav')
#elements =wd.find_elements(By.span)
for element in element:
    print(element.text)
#element.click()
input('输入回车')
wd.quit()

from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support.expected_conditions import element_to_be_selected

# 加上参数，禁止 chromedriver 日志写屏
options = webdriver.EdgeOptions()
options.add_experimental_option(
    'excludeSwitches', ['enable-logging'])

#创建webdriver对象
wd = webdriver.Edge(options=options)

wd.get('https://www.byhy.net/cdn2/files/selenium/sample1.html')
element =wd.find_elements(By.ID,'container')
spans =element.find_elements(By.TAG_NAME,'span')
for span in spans:
    print(span.text)
#element.click()
input('输入回车')
wd.quit()
import time
from time import sleep

from appium.options.common.bundle_id_option import BUNDLE_ID
from selenium.webdriver.support.expected_conditions import element_to_be_selected

from selenium import webdriver
from selenium.webdriver.common.by import By

wd = webdriver.Edge()

wd.get('https://www.byhy.net/cdn2/files/selenium/sample1.html')

#element = wd.find_element(By.ID,'container')

# 限制 选择元素的范围是 id 为 container 元素的内部。
spans = wd.find_elements(By.TAG_NAME, 'span')
for span in spans:
    print(span.text)

input('按回车退出')

wd.quit()

from selenium import webdriver
from selenium.webdriver.common.by import By
# 创建 WebDriver 对象
wd = webdriver.Edge()
wd.implicitly_wait(5)
# 调用WebDriver 对象的get方法 可以让浏览器打开指定网址
wd.get('https://www.byhy.net/cdn2/files/selenium/stock1.html')
# 根据id选择元素，返回的就是该元素对应的WebElement对象
element = wd.find_element(By.ID, 'kw')
# 通过该 WebElement对象，就可以对页面元素进行操作了
# 比如输入字符串到 这个 输入框里
element.send_keys('北方稀土')
print(element.get_attribute('value'))
element = wd.find_element(By.ID,'go')
element.click()
element = wd.find_element(By.ID,'1')
print(element.text)
print(element.get_attribute('outerHTML'))
wd.quit()
'''
#input('按回车退出')
''''from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
#from selenium.webdriver.support.ui import Select
from time import sleep
wd = webdriver.Edge()
wd.implicitly_wait(5)
wd.get("https://www.byhy.net/cdn2/files/selenium/test2.html")
# 首先获取默认选中的选项
element = wd.find_element(By.CSS_SELECTOR, '#ss_single option[selected]')
print("默认选中的值:", element.get_attribute('value'))
print("默认选中的outerHTML:", element.get_attribute('outerHTML'))
sleep(1)
# 使用Select类选择小江老师
select = Select(wd.find_element(By.ID, "ss_single"))
select.select_by_value("小江老师")
sleep(1)
# 再次获取当前选中的选项
element = select.first_selected_option
print("选择后选中的值:", element.get_attribute('value'))
print("选择后选中的outerHTML:", element.get_attribute('outerHTML'))
sleep(1)
wd.quit()'''
'''from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from time import sleep

wd = webdriver.Edge()
wd.implicitly_wait(3)
wd.get('https://www.byhy.net/cdn2/files/selenium/test2.html')
sleep(2)
select =Select(wd.find_element(By.ID,'ss_multi'))
sleep(1)
initall_select =select.all_selected_options
for option in initall_select:
    print("======初始值=====")
    print(f"{option.get_attribute('value')}")
select.deselect_all()
print('======清除所有选择======')
select.select_by_visible_text('小江老师')
sleep(1)
select.select_by_visible_text('小雷老师')
sleep(1)
print("=====最终选择======")
initall_select =select.all_selected_options
for option in initall_select:
    print(f"{option.get_attribute('value')}")
input()'''


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from time import sleep

# 初始化浏览器
wd = webdriver.Edge()
wd.implicitly_wait(3)
wd.get('https://www.byhy.net/cdn2/files/selenium/test2.html')
sleep(2)

# 创建Select对象
select = Select(wd.find_element(By.ID, 'ss_multi'))

# 1. 打印初始选中的选项
print("=== 初始选中的选项 ===")
initial_selected_options = select.all_selected_options
for option in initial_selected_options:
    print(f"值: {option.get_attribute('value')}, 文本: {option.text}")

# 2. 清除所有选项
select.deselect_all()
print("\n=== 已清除所有选项 ===")

# 3. 选择新选项
select.select_by_visible_text('小江老师')
sleep(1)
select.select_by_visible_text('小雷老师')
sleep(1)

# 4. 打印最终选中的选项
print("\n=== 最终选中的选项 ===")
final_selected_options = select.all_selected_options
for option in final_selected_options:
    print(f"值: {option.get_attribute('value')}, 文本: {option.text}")

# 保持浏览器打开
input("\n按Enter键退出...")
wd.quit()

