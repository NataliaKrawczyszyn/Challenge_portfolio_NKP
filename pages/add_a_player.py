from pages.base_page import BasePage


class AddAPlayer(BasePage):
    login_field_xpath = "//*[@id='login']"
    password_field_xpath = "//*[@id='password']"
    sign_in_button_xpath = "//*[text()='Sign in']"
    login_url = ("https://scouts-test.futbolkolektyw.pl/en/login?redirected=true")

    add_player_button_xpath = "//*[text()='Add player']"
    add_player_url = ("https://scouts-test.futbolkolektyw.pl/en/players/add")
    expected_title = "Add player"
    submit_button_xpath = "//*[text()='Submit']"
    name_field_xpath = "/html/body/div/div[1]/main/div[2]/form/div[2]/div/div[2]/div/div/input"
    surname_field_xpath = "/html/body/div/div[1]/main/div[2]/form/div[2]/div/div[3]/div/div/input"
    main_position_field_xpath = "/html/body/div/div[1]/main/div[2]/form/div[2]/div/div[11]/div/div/input"
    age_field_xpath = "/html/body/div/div[1]/main/div[2]/form/div[2]/div/div[7]/div/div/input"

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

    def click_on_the_submit_button(self):
            self.click_on_the_element(self.submit_button_xpath)

    def type_in_name(self, name):
            self.field_send_keys(self.name_field_xpath, name)

    def type_in_surname(self, surname):
            self.field_send_keys(self.surname_field_xpath, surname)

    def type_in_age(self, age):
            self.field_send_keys(self.main_position_field_xpath, age)

    def type_in_main_position(self, main_position):
            self.field_send_keys(self.age_field_xpath, main_position)

pass