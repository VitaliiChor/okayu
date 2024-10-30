from pages.contact_us_elements_functions import ContactPage


def test_checked_contact_pop_up(browser):
    contact = ContactPage(browser)
    contact.open()
    contact.click_contact_us_button()
    contact.input_field('tests@tests.com', 'Tester', 'TestTestTest')
    contact.click_send_button()
    contact.check_success_alert('Thanks for the message!!')


