from playwright.sync_api import Page


class BasePage:
    URL_PATH = ""

    def __init__(self, page):
        self.page = page
        self.base_url = "http://10.216.128.98/"
        self.nav = NavigatePage(page)

    def navigate(self):
        self.page.goto(f"{self.base_url}{self.URL_PATH}")


class NavigatePage:
    def __init__(self, page: Page):
        self.page = page
        self.dashboard_link = page.get_by_role("link", name="📊Dashboard")
        self.calibration_link = page.get_by_role("link", name="🔬Calibration")
        self.pallet_control_link = page.get_by_role("link", name="📦Pallet Control")
        self.tester_control_link = page.get_by_role("link", name="🔧Tester Control")
        self.cpk_link = page.get_by_role("link", name="📈CPK")
        self.revision_control_link = page.get_by_role("link", name="📈Revision Control")

    def go_to_dashboard(self):
        self.dashboard_link.click()

    def go_to_calibration(self):
        self.calibration_link.click()

    def go_to_pallet_control(self):
        self.pallet_control_link.click()

    def go_to_tester_control(self):
        self.tester_control_link.click()

    def go_to_cpk(self):
        self.cpk_link.click()

    def go_to_revision_control(self):
        self.revision_control_link.click()
