import unittest
import os

from pages import players_page
from pages.add_a_player import AddAPlayer

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from pages.login_page import LoginPage
from pages.players_page import PlayersPage
from pages.dashboard import Dashboard
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT

class TestPlayersPage(unittest.TestCase):
    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver_service = Service(executable_path=DRIVER_PATH)
        self.driver = webdriver.Chrome(service=self.driver_service)
        self.driver.get('https://dareit.futbolkolektyw.pl/en/login?redirected=true')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

        user_login = LoginPage(self.driver)
        user_login.type_in_email('user02@getnada.com')
        user_login.type_in_password('Test-1234')
        user_login.click_on_the_sign_in_button()
        dashboard_page = Dashboard(self.driver)
        dashboard_page.wait_for_element_to_be_clickable('/html/body/div/div[1]/div/div/div/ul[1]/div[2]/div[2]/span')
        dashboard_page.click_on_players_button()
        time.sleep(5)


    def test_players_page(self):
        players_page = PlayersPage(self.driver) #checking title of players page
        players_page.title_of_page()
        players_page.click_on_sign_out_button() #logout from players_page
        user_login = LoginPage(self.driver)
        user_login.title_of_page()

    @classmethod
    def tearDown(self):
        self.driver.quit()