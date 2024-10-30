from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage


class HomePage(BasePage):

    def __init__(self, browser):
        super().__init__(browser)

    def open(self):
        super().open('https://demoblaze.com')

    def click_galaxy_s6(self):
        self.click_element(By.XPATH, '//*[@id="tbodyid"]/div[1]/div/div/h4/a')

    def click_monitors(self):
        self.click_element(By.CSS_SELECTOR, '''[onclick="byCat('monitor')"]''')

    def click_laptops(self):
        self.click_element(By.CSS_SELECTOR, '''[onclick="byCat('notebook')"]''')

    def click_dell_laptop(self):
        self.click_element(By.XPATH, '//*[@id="tbodyid"]/div[5]/div/div/h4/a')

    def check_products_count(self, count):
        WebDriverWait(self.browser, 10).until(
            lambda driver: len(driver.find_elements(By.CSS_SELECTOR, '.card')) == count
        )
