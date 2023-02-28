import pytest
from appium.webdriver.common.appiumby import AppiumBy


@pytest.mark.usefixtures("setup")
class Test_n11_product_search:
    def test_verication_of_search_functionality(self):
        searchbar = self.driver.find_element(AppiumBy.ID, "com.dmall.mfandroid:id/tvHomeSearchBar")
        searchbar.click()

        searchbox = self.driver.find_element(AppiumBy.ID, "com.dmall.mfandroid:id/etSearch")
        searchbox.send_keys('Lenovo thinkpad')

        search_element = self.driver.find_element(AppiumBy.ID, "com.dmall.mfandroid:id/keywordTV")

        search_element.click()
