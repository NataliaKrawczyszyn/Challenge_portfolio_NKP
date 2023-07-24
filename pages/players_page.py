from pages.base_page import BasePage


class PlayersPage(BasePage):
    players_button_xpath = "/html/body/div/div[1]/div/div/div/ul[1]/div[2]/div[2]/span"
    expected_title = "Players (4264) page 1"
    players_url = "https://scouts-test.futbolkolektyw.pl/en/players"
    sign_out_button_xpath = "/html/body/div/div[1]/div/div/div/ul[2]/div[2]/div[2]/span"

    def title_of_page(self):
        assert self.get_page_title(self.players_url) == self.expected_title

    def click_on_sign_out_button(self):
        self.click_on_the_element(self.sign_out_button_xpath)


pass
