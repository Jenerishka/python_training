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

    def ensure_logout(self):
        wd = self.app.wd
        if self.is_logget_in():
            self.logout()

    def is_logget_in(self):
        wd = self.app.wd
        return len(wd.find_elements_by_link_text("Logout")) > 0

    def is_logget_in_as(self, username):
        wd = self.app.wd
        return wd.find_element_by_xpath("/html/body/div[1]/div[1]/form/b").text == username
        # return wd.find_element_by_xpath("//b[contains(.,'(admin)')]").text == username

    def login(self, username, password):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def ensure_login(self, username, password):
        wd = self.app.wd
        if self.is_logget_in():
            if self.is_logget_in_as(username):
                return
            else:
                self.logout()
        self.login(username, password)


