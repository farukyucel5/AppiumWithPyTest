from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

caps = {'platformName': 'Android', 'platformVersion': '10', 'deviceName': 'V150143202104233497',
        'automationName': 'UiAutomator2', 'appPackage': 'com.dmall.mfandroid',
        'appActivity': 'com.dmall.mfandroid.activity.base.NewSplash'}

driver = webdriver.Remote('http://localhost:4723/wd/hub', caps)

driver.implicitly_wait(30)

searchbar = driver.find_element(AppiumBy.ID, "com.dmall.mfandroid:id/tvHomeSearchBar")
searchbar.click()

searchbox = driver.find_element(AppiumBy.ID, "com.dmall.mfandroid:id/etSearch")
searchbox.send_keys('Lenovo thinkpad')

searchElement = driver.find_element(AppiumBy.ID, "com.dmall.mfandroid:id/keywordTV")

searchElement.click()
