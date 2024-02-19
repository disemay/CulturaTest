import time
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from main import element1

caps = {
    "platformName": "Android",
    "appium:platformVersion": "13",
    "appium:deviceName": "Galaxy A52",
    "appium:ensureWebviewsHavePages": True,
    "appium:nativeWebScreenshot": True,
    "appium:newCommandTimeout": 3600,
    "appium:connectHardwareKeyboard": True
}

driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)

def find_and_click_element(by, value):
    element = driver.find_element(by, value)
    element.click()

# Настройка ожидания
driver.implicitly_wait(10)

# Повторяющиеся действия с элементом element1
find_and_click_element(AppiumBy.ID, 'ru.gosuslugi.culture.test:id/vpk_btn_1')
for _ in range(7):
    element1.click()

# Последовательные действия с другими элементами
find_and_click_element(AppiumBy.ID, 'ru.gosuslugi.culture.test:id/root')
find_and_click_element(AppiumBy.ID, 'com.android.permissioncontroller:id/permission_allow_button')
find_and_click_element(AppiumBy.ID, 'ru.gosuslugi.culture.test:id/root')
find_and_click_element(AppiumBy.ID, 'com.android.permissioncontroller:id/permission_allow_one_time_button')
find_and_click_element(AppiumBy.ID, 'android:id/button2')

driver.quit()