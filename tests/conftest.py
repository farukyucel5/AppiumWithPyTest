import pytest
from appium import webdriver


@pytest.fixture(scope="class")
def setup(request):
    caps = {'platformName': 'Android', 'platformVersion': '10', 'deviceName': 'V150143202104233497',
            'automationName': 'UiAutomator2', 'appPackage': 'com.dmall.mfandroid',
            'appActivity': 'com.dmall.mfandroid.activity.base.NewSplash'}

    driver = webdriver.Remote('http://localhost:4723/wd/hub', caps)

    driver.implicitly_wait(30)
    request.cls.driver = driver
    yield
    driver.quit()
