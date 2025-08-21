from requests.utils import select_proxy
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

wd = webdriver.Edge()
wd.implicitly_wait(5)
wd.get("https://www.byhy.net/cdn2/files/selenium/sample3.html")
print(wd.window_handles)
sleep(2)
window1 =wd.window_handles[0]
selenium =wd.find_element(By.TAG_NAME,'a')
selenium.click()

window2 = None
for h in wd.window_handles:
    if h !=window1:
        window2 =h
wd.switch_to.window(window2)
print(wd.window_handles)
print(wd.title)
sou =wd.find_element(By.CSS_SELECTOR,' .sb_form_q').send_keys('白月黑羽\n')
sleep(2)
wd.close()
wd.switch_to.window(window1)
dian_ji =wd.find_element(By.ID,'outerbutton')
dian_ji.click()
sleep(2)
input('回车')
