from appium.webdriver.common.appiumby import AppiumBy

from pages.pageBase import PageBase


class N11Page(PageBase):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    searchbar = (AppiumBy.ID,"com.dmall.mfandroid:id/tvHomeSearchBar")

    def click_the_searchbar(self):
        self.wait_element_visibility(self.searchbar)
        self.driver.find_element(*self.searchbar).click()

    searchbox = (AppiumBy.ID, "com.dmall.mfandroid:id/etSearch")

    search_element = (AppiumBy.ID, "com.dmall.mfandroid:id/keywordTV")

    def type_in_product_name_and_click(self, keyword):
        self.driver.find_element(*self.searchbox).send_keys(keyword)
        self.wait_element_visibility(self.search_element)
        self.driver.find_element(*self.search_element).click()
