from model.group import Group


class GroupHelper:

    def __init__(self, app):
        self.app = app

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def fill_group_form(self, group):
        self.change_field_value("group_name", group.name)
        self.change_field_value("group_header", group.header)
        self.change_field_value("group_footer", group.footer)

    def count(self):
        wd = self.app.wd
        return len(wd.find_elements_by_name("selected[]"))

    def select_group(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def select_group_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def init_group_creation(self):
        wd = self.app.wd
        wd.find_element_by_name("new").click()

    def init_group_modification(self):
        wd = self.app.wd
        wd.find_element_by_name("edit").click()

    def submit_group_creation(self):
        wd = self.app.wd
        wd.find_element_by_name("submit").click()

    def submit_group_modification(self):
        wd = self.app.wd
        wd.find_element_by_name("update").click()

    def submit_group_deletion(self):
        wd = self.app.wd
        wd.find_element_by_name("delete").click()

    def create(self, group):
        self.app.goto.groups_page()
        self.init_group_creation()
        self.fill_group_form(group)
        self.submit_group_creation()
        self.return_to_groups_page()
        self.group_cache = None

    def create_if_required(self, group):
        self.app.goto.groups_page()
        if self.count() == 0:
            self.create(group)

    def modify_first_group(self, group):
        self.modify_group_by_index(0, group)

    def modify_group_by_index(self, index, group):
        self.app.goto.groups_page()
        self.select_group_by_index(index)
        self.init_group_modification()
        self.fill_group_form(group)
        self.submit_group_modification()
        self.return_to_groups_page()
        self.group_cache = None

    def delete_first_group(self):
        self.delete_group_by_index(0)

    def delete_group_by_index(self, index):
        self.app.goto.groups_page()
        self.select_group_by_index(index)
        self.submit_group_deletion()
        self.return_to_groups_page()
        self.group_cache = None

    def return_to_groups_page(self):
        self.app.goto.groups_page()

    group_cache = None

    def get_group_list(self):
        if self.group_cache is None:
            wd = self.app.wd
            self.app.goto.groups_page()
            self.group_cache = []
            for element in wd.find_elements_by_css_selector("span.group"):
                id = element.find_element_by_name("selected[]").get_attribute("value")
                name = element.text
                self.group_cache.append(Group(name=name, id=id))
        return list(self.group_cache)
