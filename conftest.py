import pytest
from pages.dashboard_page import DashboardPage
from pages.calibration_page import CalibrationPage
from pages.pallet_control_page import PMPalletPage
from pages.revision_control_page import RevisionPage
from pages.tester_control_page import TesterPage


# Fixture Dashboard
@pytest.fixture
def dashboard(page):
    pg = DashboardPage(page)
    pg.navigate()
    return pg


# Fixture Calibration
@pytest.fixture
def calibration(page):
    pg = CalibrationPage(page)
    pg.navigate()
    return pg


# Fixture Pallet Control
@pytest.fixture
def pallet_page(page):
    pg = PMPalletPage(page)
    pg.navigate()
    return pg


# Fixture Tester Control
@pytest.fixture
def tester_page(page):
    pg = TesterPage(page)
    pg.navigate()
    return pg


# Fixture Revision Control
@pytest.fixture
def revision_page(page):
    pg = RevisionPage(page)
    pg.navigate()
    return pg
