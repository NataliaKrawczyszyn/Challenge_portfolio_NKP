from pages.base_page import BasePage
from selenium.common.exceptions import NoSuchElementException

class LoginPage(BasePage):
    login_field_xpath = "//*[@id='login']"
    password_field_xpath = "//*[@id='password']"
    sign_in_button_xpath = "//*[text()='Sign in']"
    login_url = ("https://dareit.futbolkolektyw.pl/en/login?redirected=true")
    expected_title = "Scouts panel - sign in"
    invalid_password_text_xpath = "/html/body/div/form/div/div[1]/div[3]/span"
    change_language_button_xpath = "/html/body/div/form/div/div[2]/div/div"
    polski_button_xpath = "/html/body/div[2]/div[3]/ul/li[1]"
    zaloguj_button_xpath= "//*[text()='Zaloguj']"


    def type_in_email(self, email):
        self.field_send_keys(self.login_field_xpath, email)

    def type_in_password(self, password):
        self.field_send_keys(self.password_field_xpath, password)

    def click_on_the_sign_in_button(self):
        self.click_on_the_element(self.sign_in_button_xpath)

    def title_of_page(self):
        assert self.get_page_title(self.login_url) == self.expected_title

    def find_validation_text(self):
        self.find_element(self.invalid_password_text_xpath)

    def change_language(self):
        self.click_on_the_element(self.change_language_button_xpath)

    def click_on_polski_button(self):
        self.click_on_the_element(self.polski_button_xpath)









