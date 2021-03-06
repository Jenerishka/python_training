from selenium import webdriver
from fixture.session import SessionHelper
from fixture.contact import ContactHelper
from fixture.group import GroupHelper


class Application:

    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(5)
        self.session = SessionHelper(self)
        self.contact = ContactHelper(self)
        self.group = GroupHelper(self)

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def return_to_home_page(self):
        wd = self.wd
        wd.find_element_by_link_text("home page").click()

    def open_home_page(self):
        wd = self.wd
        # wd.get("http://localhost/addressbook/")
        if not (wd.current_url.endswith("/addressbook/") and not len(wd.find_elements_by_link_text("Create account")) > 0):
            wd.get("http://localhost/addressbook/")

    def destroy(self):
        self.wd.quit()