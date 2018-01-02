class NavigationHelper:

    def __init__(self, app):
        self.app = app

    def home_page(self, base_url):
        wd = self.app.wd
        if wd.current_url == base_url and len(wd.find_elements_by_name("searchform")) > 0:
            return
        wd.get(base_url)

    def groups_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/group.php") and len(wd.find_elements_by_name("new")) > 0):
            wd.find_element_by_link_text("groups").click()
