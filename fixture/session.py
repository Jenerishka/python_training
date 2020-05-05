class SessionHelper:

    def __init__(self, app):
        self.app = app

    def logout(self, NoSuchElementExeption=None):
        wd = self.app.wd
        try:
            elem = wd.find_element_by_link_text("Logout")
            elem.click()
            wd.find_element_by_name("user")
        except NoSuchElementExeption:
            print("ops")

    def login(self, username, password):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()
