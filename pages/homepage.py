from telnetlib import EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class HomePage:

    def __init__(self, browser):
        self.browser = browser


    def open(self):
       self.browser.get('https://demoblaze.com')

    def click_galaxy_s6(self):
        galaxy_s6 = self.browser.find_element(By.XPATH, '//*[@id="tbodyid"]/div[1]/div/div/h4/a')
        galaxy_s6.click()

    def click_monitors(self):
        monitors = self.browser.find_element(By.CSS_SELECTOR, '''[onclick="byCat('monitor')"]''')
        monitors.click()

    def click_laptops(self):
        laptops = self.browser.find_element(By.CSS_SELECTOR, '''[onclick="byCat('notebook')"]''')
        laptops.click()

    def click_dell_laptop(self):
        laptop_dell = self.browser.find_element(By.XPATH, '//*[@id="tbodyid"]/div[5]/div/div/h4/a')
        laptop_dell.click()

    def check_products_count(self, count):
        WebDriverWait(self.browser, 10).until(
            lambda driver: len(driver.find_elements(By.CSS_SELECTOR, '.card')) == count
        )
