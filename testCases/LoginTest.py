import unittest
import HtmlTestRunner

from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service

import sys
sys.path.append("C://Users//vivek.s07//PycharmProjects//pythonProject1_POMbased")
from pageObjects.LoginPage import LoginPage

class LoginTest(unittest.TestCase):
    userName = "Robert@barca.com"
    password = "Lewandowski@Muller9"
    url = "https://practice.automationtesting.in/my-account/"
    s = Service('D:\selenium webdrivers\chromedriver.exe')
    driver = webdriver.Chrome(service=s)
# Sample cred: Robert@barca.com - Lewandowski@Muller9
    @classmethod
    def setUpClass(cls):
        cls.driver.get(cls.url)
        cls.driver.maximize_window()


    def test_Login(self):
        lp1 = LoginPage(self.driver)
        lp1.typeUserName(self.userName)
        lp1.typePassword(self.password)
        lp1.clickLoginButton()
        time.sleep(5)
        self.assertEqual("My Account – Automation Practice Site",self.driver.title,"Not the page we were looking for")

    @unittest.skip
    def test_skip(self):
        self.assertTrue(True)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='..\\reports'))