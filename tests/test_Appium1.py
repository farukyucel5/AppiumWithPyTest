import pytest

from pages.n11Page import N11Page


@pytest.mark.usefixtures("setup")
class Test_n11_product_search:

    def test_verication_of_search_functionality(self):
        n11_page = N11Page(self.driver)
        n11_page.click_the_searchbar()
        n11_page.type_in_product_name_and_click("Lenovo thinkpad")
