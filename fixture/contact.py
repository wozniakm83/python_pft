from model.contact import Contact


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def fill_contact_form(self, contact):
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)
        self.change_field_value("title", contact.title)
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.address)
        self.change_field_value("home", contact.home)
        self.change_field_value("mobile", contact.mobile)
        self.change_field_value("work", contact.work)
        self.change_field_value("fax", contact.fax)
        self.change_field_value("email", contact.email)
        self.change_field_value("email2", contact.email2)
        self.change_field_value("email3", contact.email3)
        self.change_field_value("homepage", contact.homepage)

    def count(self):
        wd = self.app.wd
        return len(wd.find_elements_by_name("entry"))

    def select_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def select_group(self):
        wd = self.app.wd
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[@name='new_group']//option[1]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[@name='new_group']//option[1]").click()

    def init_contact_creation(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//*[@id='nav']/ul/li[2]/a").click()

    def init_contact_modification(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//*[@id='maintable']/tbody/tr[2]/td[8]/a/img").click()

    def submit_contact_creation(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def submit_contact_modification(self):
        wd = self.app.wd
        wd.find_element_by_name("update").click()

    def submit_contact_deletion(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//*[@id='content']/form[2]/div[2]/input").click()

    def confirm_contact_deletion(self):
        wd = self.app.wd
        wd.switch_to_alert().accept()

    def create(self, contact):
        self.app.goto.home_page()
        self.init_contact_creation()
        self.fill_contact_form(contact)
        self.select_group()
        self.submit_contact_creation()
        self.return_to_home_page()
        self.contact_cache = None

    def create_if_required(self, contact):
        self.app.goto.home_page()
        if self.count() == 0:
            self.create(contact)

    def modify(self, contact):
        self.app.goto.home_page()
        self.select_contact()
        self.init_contact_modification()
        self.fill_contact_form(contact)
        self.submit_contact_modification()
        self.return_to_home_page()
        self.contact_cache = None

    def delete(self):
        self.app.goto.home_page()
        self.select_contact()
        self.submit_contact_deletion()
        self.confirm_contact_deletion()
        self.return_to_home_page()
        self.contact_cache = None

    def return_to_home_page(self):
        self.app.goto.home_page()

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.app.goto.home_page()
            self.contact_cache = []
            for element in wd.find_elements_by_name("entry"):
                id = element.find_element_by_name("selected[]").get_attribute("value")
                firstname = element.find_element_by_css_selector("td:nth-child(3)").text
                lastname = element.find_element_by_css_selector("td:nth-child(2)").text
                self.contact_cache.append(Contact(firstname=firstname, lastname=lastname, id=id))
        return list(self.contact_cache)
