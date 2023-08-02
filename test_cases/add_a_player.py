import unittest
import os
from pages.add_a_player import AddAPlayer

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from pages.login_page import LoginPage
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT

class TestAddAPlayer(unittest.TestCase):

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
        time.sleep(5)

    def test_add_a_player(self):
        add_player = AddAPlayer(self.driver)
        add_player.click_on_the_add_player_button()
        add_player.title_of_page()

        add_player.type_in_name('Edward') #adding a player Edward Ziemba
        add_player.type_in_surname('Ziemba')
        add_player.type_in_age('25.12.1995')
        add_player.type_in_main_position('Goalkeeper')
        add_player.click_on_the_submit_button()




    @classmethod
    def tearDown(self):
        self.driver.quit()