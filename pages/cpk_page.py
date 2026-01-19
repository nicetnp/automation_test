from pages.dashboard_navigate_page import NavigatePage, BasePage


class CPKPage(BasePage):
    URL_PATH = "one-day-search"

    def __init__(self, page):
        super().__init__(page)
        self.nav = NavigatePage(page)
        self.heading = page.get_by_role("heading", name="SPC & Process Capability")

    def expect_page(self):
        from playwright.sync_api import expect
        expect(self.heading).to_be_visible()
