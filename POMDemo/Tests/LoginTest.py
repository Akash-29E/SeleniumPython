import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from POMDemo.Pages.loginPage import LoginPage
from POMDemo.Pages.homePage import HomePage
import HtmlTestRunner
class LoginTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome(ChromeDriverManager().install())
        cls.driver.implicitly_wait(10)

    def test_Login(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")

        login = LoginPage(driver)
        login.enter_username("standard_user")
        login.enter_password("secret_sauce")
        login.click_login()

        homepage = HomePage(driver)
        homepage.OpenSidebar()
        homepage.LogoutClick()
        # self.driver.find_element_by_id("user-name").send_keys("standard_user")
        # self.driver.find_element_by_id("password").send_keys("secret_sauce")
        # self.driver.find_element_by_id("login-button").click()
        # self.driver.find_element_by_class_name("bm-burger-button").click()
        # self.driver.find_element_by_id("logout_sidebar_link").click()
        time.sleep(2)
        print("Test Completed!")


    @classmethod
    def tearDownClass(cls) -> None:

        cls.driver.close()
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="C:/Users/Akash/PycharmProjects/Selenium/Reports"))

