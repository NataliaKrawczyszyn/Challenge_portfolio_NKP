import os
import time
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from pages.dashboard import Dashboard
from pages.login_page import LoginPage
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT


class TestLoginPage(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver_service = Service(executable_path=DRIVER_PATH)
        self.driver = webdriver.Chrome(service=self.driver_service)
        self.driver.get('https://dareit.futbolkolektyw.pl/en/login?redirected=true')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)
    def test_log_in_to_the_system(self): #log in with valid login and invalid password
        user_login = LoginPage(self.driver)  # log in with valid login and valid password
        # user_login.title_of_page()
        user_login.type_in_email('user02@getnada.com')
        user_login.type_in_password('Test-1234')
        user_login.wait_for_element_to_be_clickable("//*[text()='Sign in']")
        user_login.click_on_the_sign_in_button()
        dashboard_page = Dashboard(self.driver)
        dashboard_page.title_of_page()

        user_login = LoginPage(self.driver)
        #user_login.title_of_page()
        user_login.type_in_email('user02@getnada.com')
        user_login.type_in_password('Invalid1234')
        user_login.wait_for_element_to_be_clickable("//*[text()='Sign in']")
        user_login.click_on_the_sign_in_button()
        user_login.find_validation_text() #checking if validation text appears



    @classmethod
    def tearDown(self):
        self.driver.quit()

