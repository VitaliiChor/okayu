from pages.homepage_functions import HomePage
from pages.product import ProductPage


def test_open_s6(browser):
    homepage = HomePage(browser)
    homepage.open()
    homepage.click_galaxy_s6()
    product_page = ProductPage(browser)
    product_page.check_title_is('Samsung galaxy s6')

def test_click_on_laptop_after_checking_count(browser):
    homepage = HomePage(browser)
    homepage.open()
    homepage.click_laptops()
    homepage.check_products_count(6)
    homepage.click_dell_laptop()

def test_count_of_monitors(browser):
    homepage = HomePage(browser)
    homepage.open()
    homepage.click_monitors()
    homepage.check_products_count(2)
