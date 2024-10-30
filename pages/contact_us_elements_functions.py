from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class ContactPage(BasePage):

    def __init__(self, browser):
        super().__init__(browser)

    def open(self):
        super().open('https://demoblaze.com')

    def click_contact_us_button(self):
        self.click_element(By.XPATH, '//*[@id="navbarExample"]/ul/li[2]/a')

    def input_field(self, email, name, message):
        email_field = self.browser.find_element(By.ID, 'recipient-email')
        email_field.send_keys(email)

        email_field = self.browser.find_element(By.ID, 'recipient-name')
        email_field.send_keys(name)

        email_field = self.browser.find_element(By.ID, 'message-text')
        email_field.send_keys(message)

    def click_send_button(self):
        self.click_element(By.XPATH, '//*[@id="exampleModal"]/div/div/div[3]/button[2]')