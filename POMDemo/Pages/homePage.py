from POMDemo.Locators.locators import Locators
class HomePage():

    def __init__(self, driver):
        self.driver = driver

        self.overflow_link_classname = "bm-burger-button"
        self.logout_link_id = "logout_sidebar_link"

    def OpenSidebar(self):
        self.driver.find_element_by_class_name(self.overflow_link_classname).click()

    def LogoutClick(self):
        self.driver.find_element_by_id(self.logout_link_id).click()