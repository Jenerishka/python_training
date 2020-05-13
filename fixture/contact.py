from selenium.webdriver.support.select import Select


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def create(self, contact):
        wd = self.app.wd
        # create new contact
        self.open_add_new_page()
        # create new contact
        # work with the form
        self.forms_change(contact)
        # Select group
        wd.find_element_by_name("new_group").click()
        Select(wd.find_element_by_name("new_group")).select_by_visible_text(contact.group)
        # submit contact creation
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.app.return_to_home_page()

    def forms_change(self, contact):
        wd = self.app.wd
        self.change_form_value_contact("firstname", contact.firstname)
        self.change_form_value_contact("middlename", contact.middlename)
        self.change_form_value_contact("lastname", contact.lastname)
        self.change_form_value_contact("nickname", contact.nickname)
        self.change_form_value_contact("company", contact.company)
        self.change_form_value_contact("title", contact.title)
        self.change_form_value_contact("address", contact.address)
        self.change_form_value_contact("mobile", contact.mobile)
        self.change_form_value_contact("home", contact.home)
        self.change_form_value_contact("work", contact.work)
        self.change_form_value_contact("fax", contact.fax)
        self.change_form_value_contact("email", contact.email)
        self.change_form_value_contact("email2", contact.email2)
        self.change_form_value_contact("email3", contact.email3)
        self.change_form_value_contact("homepage", contact.homepage)
        self.type("bday", contact.bday)
        self.type("bmonth", contact.bmonth)
        self.type("aday", contact.aday)
        self.type("amonth", contact.amonth)
        self.change_form_value_contact("byear", contact.Birthdayyear)
        self.change_form_value_contact("ayear", contact.Anniversaryyear)
        self.change_form_value_contact("address2", contact.address2)
        self.change_form_value_contact("phone2", contact.phone2)
        self.change_form_value_contact("notes", contact.notes)

    def type(self, field_select, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_select).click()
            Select(wd.find_element_by_name(field_select)).select_by_visible_text\
                (text)

    def change_form_value_contact(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def delete_first_contact(self):
        wd = self.app.wd
        self.press_button_edit()
        # press button delete
        wd.find_element_by_xpath("/html/body/div[1]/div[4]/form[2]/input[2]").click()

    def press_button_edit(self):
        wd = self.app.wd
        wd.find_element_by_xpath(
            "/html/body/div[1]/div[4]/form[2]/table/tbody/tr[2]/td[8]/a/img").click()

    def modific_first_contact(self, contact):
        wd = self.app.wd
        # press button edit
        self.press_button_edit()
        # work with the form
        self.forms_change(contact)
        # _submit contact creation
        wd.find_element_by_name("update").click()
        self.app.return_to_home_page()

    def open_add_new_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def count(self):
        wd = self.app.wd
        # self.group.return_to_general_home_page()
        wd.find_element_by_link_text("home").click()
        return len(wd.find_elements_by_name("selected[]"))

