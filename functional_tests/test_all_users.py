# -*- coding: utf-8 -*-

from selenium import webdriver
from django.core.urlresolvers import reverse
from django.contrib.staticfiles.testing import StaticLiveServerTestCase

from pyvirtualdisplay import Display

class HomeNewVisitorTest(StaticLiveServerTestCase):

    def setUp(self):
        self.display = Display(visible=0, size=(1024, 768))
        self.display.start()
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()
        self.display.stop()

    def get_full_url(self, namespace):
        return self.live_server_url + reverse(namespace)

    def test_home_title(self):
        self.browser.get(self.get_full_url("home"))
        self.assertIn("TaskBuster", self.browser.title)

    def test_h1_css(self):
        self.browser.get(self.get_full_url("home"))
        h1 = self.browser.find_element_by_tag_name("h1")
        self.assertEqual(h1.value_of_css_property("color"), "rgba(200, 50, 255, 1)")
