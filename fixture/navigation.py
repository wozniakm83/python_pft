class NavigationHelper:

    def __init__(self, app):
        self.app = app

    def home_page(self):
        wd = self.app.wd
        wd.get("http://localhost/addressbook/")

    def groups_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()
