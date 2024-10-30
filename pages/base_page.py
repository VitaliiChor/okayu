from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, browser):
        self.browser = browser

    def open(self, url):
        self.browser.get(url)

    def click_element(self, by, locator):
        element = self.browser.find_element(by, locator)
        element.click()

    def check_success_alert(self, expected_message):
        alert = WebDriverWait(self.browser, 10).until(EC.alert_is_present())
        alert_text = alert.text

        assert expected_message in alert_text, f'Expected "{expected_message}" but got "{alert_text}"'
