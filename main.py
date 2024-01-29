import time
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput

caps = {}
caps["platformName"] = "Android"
caps["appium:platformVersion"] = "13"
caps["appium:deviceName"] = "Galaxy A52"
caps["appium:ensureWebviewsHavePages"] = True
caps["appium:nativeWebScreenshot"] = True
caps["appium:newCommandTimeout"] = 3600
caps["appium:connectHardwareKeyboard"] = True

driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)

element = driver.find_element(AppiumBy.ID, 'ru.gosuslugi.culture.test:id/root')
element.click()

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver.implicitly_wait(10)

element1 = driver.find_element(AppiumBy.ID, 'ru.gosuslugi.culture.test:id/vpk_btn_1')
element1.click()
element1.click()
element1.click()
element1.click()
element1.click()
element1.click()
element1.click()
element1.click()

element2 = driver.find_element(AppiumBy.ID, 'ru.gosuslugi.culture.test:id/root')
element2.click()

element3 = driver.find_element(AppiumBy.ID, 'com.android.permissioncontroller:id/permission_allow_button')
element3.click()

element4 = driver.find_element(AppiumBy.ID, 'ru.gosuslugi.culture.test:id/root')
element4.click()

element5 = driver.find_element(AppiumBy.ID, 'com.android.permissioncontroller:id/permission_allow_one_time_button')
element5.click()

element6 = driver.find_element(AppiumBy.ID, 'android:id/button2')
element6.click()







driver.quit()