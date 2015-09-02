# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest
from pyvirtualdisplay import Display


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        
        self.display = Display(visible=0, size=(1024, 768))
        self.display.start()
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()
        self.display.stop()

    def test_it_worked(self):
        self.browser.get("http://localhost:8000")
        self.assertIn("Welcome to Django", self.browser.title)

if __name__ == '__main__':
    unittest.main(warnings='ignore')
