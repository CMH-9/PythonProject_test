'''from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options

def real_device_test():
    # 1. 创建Options对象（新版API）
    options = UiAutomator2Options()
    # 2. 设置必要能力
    options.platform_name = "Android"
    options.automation_name = "UIAutomator2"  # 修正：不能是"Android"，必须是有效的引擎
    options.device_name = "127.0.0.1:7555"    # 注意：这里可能应该是device_name（拼写检查）
    options.platform_version = "12"           # 注意：属性名是platform_version（小写）
    options.app_package = "com.tencent.mobileqq"
    options.app_activity = ".activity.SplashActivity"
    # 3. 添加额外能力（如果需要）
    # options.new_command_timeout = 300  # 设置新命令超时时间（单位秒）

    try:
        # 4. 使用options创建驱动
        driver = webdriver.Remote(
            command_executor='http://localhost:4723/wd/hub', # 确保Appium服务运行在此地址
            options=options
        )
        print("设备连接成功！")

        # 5. 添加等待确保元素加载（重要！）
        driver.implicitly_wait(10)  # 修正拼写：implicitly

        # 6. 修正元素定位语法
        # 示例：点击包含“网络”文本的元素
        network_element = driver.find_element(
            AppiumBy.XPATH,
            "//*[contains(@text, '网络')]"  # 修正XPath表达式
        )
        network_element.click()
        print("界面元素操作成功！")

        # 7. 打印当前Activity
        print(f"当前Activity: {driver.current_activity}")

        driver.quit()
        print("自动化测试成功！")
        return True
    except Exception as e:
        print(f"自动化测试失败: {str(e)}")
        return False

if __name__ == "__main__":
    if real_device_test():
        print("环境配置正确，可进行自动化操作")
    else:
        print("需要检查环境配置")'''
from appium import webdriver
from selenium.webdriver.common.by import By
from appium.webdriver.extensions.android.nativekey import AndroidKey
from appium.options.android import UiAutomator2Options

desired_caps = {
  'platformName': 'Android', # 被测手机是安卓
  'platformVersion': '12', # 手机安卓版本，如果是鸿蒙系统，依次尝试 12、11、10 这些版本号
  'deviceName': '程明辉', # 设备名，安卓手机可以随意填写
  'appPackage': 'tv.danmaku.bili', # 启动APP Package名称
  'appActivity': '.MainActivityV2', # 启动Activity名称
  'unicodeKeyboard': True, # 自动化需要输入中文时填True
  'resetKeyboard': True, # 执行完程序恢复原来输入法
  'noReset': True,       # 不要重置App
  'newCommandTimeout': 6000,
  'automationName' : 'UiAutomator2'
  # 'app': r'd:\apk\bili.apk',
}

# 连接Appium Server，初始化自动化环境
driver = webdriver.Remote('http://localhost:4723/wd/hub',
  options=UiAutomator2Options().load_capabilities(desired_caps))

# 设置缺省等待时间
driver.implicitly_wait(5)

# 如果有`青少年保护`界面，点击`我知道了`
iknow = driver.find_elements(By.ID, "text3")
if iknow:
    iknow.click()

# 根据id定位搜索位置框，点击
driver.find_element(By.ID, 'expand_search').click()

# 根据id定位搜索输入框，点击
sbox = driver.find_element(By.ID, 'search_src_text')
sbox.send_keys('大象新闻')
# 输入回车键，确定搜索
driver.press_keycode(AndroidKey.ENTER)

# 选择（定位）所有视频标题
eles = driver.find_elements(By.ID, 'title')

for ele in eles:
    # 打印标题
    print(ele.text)

input('**** Press to quit..')
driver.quit()