from selenium.webdriver.firefox.webdriver import WebDriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.contact import ContactHelper
from fixture.navigation import NavigationHelper


class Application:

    def __init__(self):
        self.wd = WebDriver(capabilities={"marionette": False})
        """self.wd = WebDriver(capabilities={"marionette": False},
                            firefox_binary="C:/Program Files (x86)/Mozilla Firefox ESR/firefox.exe")"""
        self.wd.implicitly_wait(5)
        self.session = SessionHelper(self)
        self.goto = NavigationHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def destroy(self):
        self.wd.quit()
