from pages.dashboard_navigate_page import NavigatePage, BasePage


class PMPalletPage(BasePage):
    URL_PATH = "pm-pallet"

    def __init__(self, page):
        super().__init__(page)
        self.nav = NavigatePage(page)
        self.heading = page.get_by_role("heading", name="PM Pallet Management")

    def expect_page(self):
        from playwright.sync_api import expect
        expect(self.heading).to_be_visible()
