import unittest

from unittest.loader import makeSuite
from unittest.loader import TestLoader

# from test_cases.fill_in_a_form import TestFillInaForm

from test_cases.add_a_player import TestAddAPlayer
from test_cases.change_language import TestChangeLanguage
from test_cases.framework import Test, TestMediumPage
from test_cases.log_in_to_the_system import TestLoginPage
from test_cases.players_page import TestPlayersPage


def full_suite():
   test_suite = unittest.TestSuite()
   test_suite.addTest(makeSuite(TestLoginPage))
   test_suite.addTest(makeSuite(TestAddAPlayer))
   test_suite.addTest(makeSuite(TestChangeLanguage))
   test_suite.addTest(makeSuite(TestMediumPage))
   test_suite.addTest(makeSuite(TestPlayersPage))
   test_suite.addTest(makeSuite(TestAddAPlayer))
   return test_suite

if __name__ == '__main__':
   runner = unittest.TextTestRunner(verbosity=2)
   runner.run(full_suite())