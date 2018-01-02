from model.contact import Contact
import re


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
        self.change_field_value("phone2", contact.phone2)
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

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def select_group(self):
        wd = self.app.wd
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[@name='new_group']//option[1]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[@name='new_group']//option[1]").click()

    def init_contact_creation(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//*[@id='nav']/ul/li[2]/a").click()

    def init_contact_modification(self, contact):
        wd = self.app.wd
        wd.find_element_by_css_selector("a[href='edit.php?id=" + str(contact.id) + "']").click()

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

    def modify_first_contact(self, contact):
        self.modify_contact_by_index(0, contact)

    def modify_contact_by_index(self, index, contact):
        self.app.goto.home_page()
        self.select_contact_by_index(index)
        self.init_contact_modification(contact)
        self.fill_contact_form(contact)
        self.submit_contact_modification()
        self.return_to_home_page()
        self.contact_cache = None

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        self.app.goto.home_page()
        self.select_contact_by_index(index)
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
            for row in wd.find_elements_by_name("entry"):
                cells = row.find_elements_by_tag_name("td")
                id = cells[0].find_element_by_tag_name("input").get_attribute("value")
                lastname = cells[1].text
                firstname = cells[2].text
                address = cells[3].text
                all_emails = cells[4].text
                all_phones = cells[5].text
                self.contact_cache.append(Contact(id=id, firstname=firstname, lastname=lastname, address=address,
                                                  all_emails=all_emails, all_phones=all_phones))
        return list(self.contact_cache)

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.app.goto.home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.app.goto.home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        id = wd.find_element_by_name("id").get_attribute("value")
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        home = wd.find_element_by_name("home").get_attribute("value")
        mobile = wd.find_element_by_name("mobile").get_attribute("value")
        work = wd.find_element_by_name("work").get_attribute("value")
        phone2 = wd.find_element_by_name("phone2").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        return Contact(id=id, firstname=firstname, lastname=lastname, address=address,
                       home=home, mobile=mobile, work=work, phone2=phone2,
                       email=email, email2=email2, email3=email3)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        home = re.search("H: (.*)", text).group(1)
        work = re.search("W: (.*)", text).group(1)
        mobile = re.search("M: (.*)", text).group(1)
        phone2 = re.search("P: (.*)", text).group(1)
        return Contact(home=home, mobile=mobile, work=work, phone2=phone2)



