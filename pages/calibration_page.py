from pages.dashboard_navigate_page import NavigatePage, BasePage
import re


class CalibrationPage(BasePage):
    URL_PATH = "calibration"

    def __init__(self, page):
        super().__init__(page)
        self.nav = NavigatePage(page)
        self.heading = page.get_by_role("heading", name=re.compile("Calibration Management", re.IGNORECASE))

    def expect_page(self):
        from playwright.sync_api import expect
        expect(self.heading).to_be_visible()
