from pages.base_page import BasePage


class AddAPlayer(BasePage):
    login_field_xpath = "//*[@id='login']"
    password_field_xpath = "//*[@id='password']"
    sign_in_button_xpath = "//*[text()='Sign in']"
    login_url = ("https://scouts-test.futbolkolektyw.pl/en/login?redirected=true")

    add_player_button_xpath = "/html/body/div/div[1]/main/div[3]/div[2]/div/div/a/button/span[1]"
    add_player_url = ("https://scouts-test.futbolkolektyw.pl/en/players/add")
    expected_title = "Add player"


    def click_on_the_add_player_button(self):
        self.click_on_the_element(self.add_player_button_xpath)

    def title_of_page(self):
        assert self.get_page_title(self.add_player_url) == self.expected_title

    def type_in_email(self, email):
            self.field_send_keys(self.login_field_xpath, email)

    def type_in_password(self, password):
            self.field_send_keys(self.password_field_xpath, password)

    def click_on_the_sign_in_button(self):
            self.click_on_the_element(self.sign_in_button_xpath)

pass