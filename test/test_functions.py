
from pages.homepage import HomePage
from pages.product import ProductPage





def test_open_s6(browser):
    homepage = HomePage(browser)
    homepage.open()
    homepage.click_galaxy_s6()
    product_page = ProductPage(browser)
    product_page.check_title_is('Samsung galaxy s6')

def test_count_of_monitors(browser):
    homepage = HomePage(browser)
    homepage.open()
    homepage.click_monitors()
    homepage.check_products_count(2)
