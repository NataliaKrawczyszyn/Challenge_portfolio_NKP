from pages.base_page import BasePage
import time

class Dashboard(BasePage):
    main_page_button_xpath = "/html/body/div/div[1]/div/div/div/ul[1]/div[1]/div[2]/span"
    players_button_xpath = "/html/body/div/div[1]/div/div/div/ul[1]/div[2]/div[2]/span"
    language_button_xpath = "/html/body/div/div[1]/div/div/div/ul[2]/div[1]/div[2]/span"
    players_count_field_xpath = "/html/body/div/div[1]/main/div[2]/div[1]/div/div[1]"
    matches_count_field_xpath = "/html/body/div/div[1]/main/div[2]/div[2]/div"
    reports_count_field_xpath = "/html/body/div/div[1]/main/div[2]/div[3]/div/div[2]"
    events_count_field_xpath = "/html/body/div/div[1]/main/div[2]/div[4]/div/div[1]"
    dev_team_contact_button_xpath = "/html/body/div/div[1]/main/div[3]/div[1]/div/div[3]/a/span[1]"
    futbol_kolektyw_image_xpath = "/html/body/div/div[1]/main/div[3]/div[1]/div/div[1]"
    add_player_button_xpath = "/html/body/div/div[1]/main/div[3]/div[2]/div/div/a/button/span[1]"
    expected_title = "Scouts panel"
    dashboard_url = "https://scouts-test.futbolkolektyw.pl/"

    def title_of_page(self):
        time.sleep(5)
        assert self.get_page_title(self.dashboard_url) == self.expected_title
pass