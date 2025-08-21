

#Sauce Labs Demo电商流程测试（Python+Selenium自动化）
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

cmh =webdriver.Edge()# 创建 WebDriver 对象
cmh.implicitly_wait(5)#隐式等待5秒
cmh.get('https://www.saucedemo.com/')#调用WebDriver 对象的get方法，打开指定网址
user =cmh.find_element(By.CSS_SELECTOR,'[placeholder="Username"]')#根据css表达式，定位用户名输入框的元素
user.click()#点击
user.send_keys('standard_user')#输入用户名
#等待一秒
sleep(1)
pwd =cmh.find_element(By.CSS_SELECTOR,'#password')#根据css表达式，定位密码输入框的元素
pwd.click()#点击
pwd.send_keys('secret_sauce')#输入密码
#等待一秒
sleep(1)
deng_lu =cmh.find_element(By.ID,'login-button')#根据ID选择元素，定位登录按钮的元素
deng_lu.click()#点击
#等待一秒
sleep(1)
add1 = cmh.find_element(By.CSS_SELECTOR,'#add-to-cart-sauce-labs-backpack')#根据css表达式，定位指定商品加入购物车
add1.click()#点击
#等待一秒
sleep(1)
add2 = cmh.find_element(By.CSS_SELECTOR,'#add-to-cart-sauce-labs-fleece-jacket')#根据css表达式，定位指定商品加入购物车
add2.click()
#等待一秒
sleep(1)
#根据css表达式，定位指定商品加入购物车并进行点击
cmh.find_element(By.CSS_SELECTOR,'[name="add-to-cart-sauce-labs-bike-light"]').click()
#等待一秒
sleep(1)
shopping = cmh.find_element(By.CSS_SELECTOR,'.shopping_cart_link')#根据css表达式，定位购物车按钮的元素
shopping.click()#点击
sleep(1)#等待一秒
checkout= cmh.find_element(By.ID,'checkout')#根据class属性选择商品提交按钮
checkout.click()#点击
sleep(1)#等待一秒
input_M= cmh.find_element(By.CSS_SELECTOR,'[data-test="firstName"]')#根据css表达式，定位收货人‘名字’输入框的元素
input_M.click()
sleep(1)
input_M.send_keys('三')
input_X = cmh.find_element(By.CSS_SELECTOR,'[data-test="lastName"]')#根据css表达式，定位收货人‘姓’输入框的元素
input_X.click()
sleep(1)
input_X.send_keys('张')
input_Y_b = cmh.find_element(By.ID,'postal-code')
input_Y_b.send_keys('666666')
sleep(1)
#根据css表达式，定位continue元素
continue_c =cmh.find_element(By.CSS_SELECTOR,'[data-test="continue"]')
continue_c.click()
sleep(1)
#根据css表达式，定位finish元素
finish_f = cmh.find_element(By.CSS_SELECTOR,'[data-test="finish"]')
finish_f.click()
sleep(1)
#根据ID属性定位‘返回’按钮元素并进行点击
cmh.find_element(By.ID,'back-to-products').click()
sleep(1)
#关闭该网页
cmh.close()
input()
