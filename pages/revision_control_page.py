from pages.dashboard_navigate_page import NavigatePage, BasePage


class RevisionPage(BasePage):
    URL_PATH = "prog-revision"

    def __init__(self, page):
        super().__init__(page)
        self.nav = NavigatePage(page)
        self.heading = page.get_by_role("heading", name="Program Revision Control")

    def expect_page(self):
        from playwright.sync_api import expect
        expect(self.heading).to_be_visible()
