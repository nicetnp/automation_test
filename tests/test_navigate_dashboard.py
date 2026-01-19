def test_nav_dashboard(dashboard):
    dashboard.expect_page()


def test_nav_calibration(calibration):
    calibration.expect_page()


def test_nav_pallet_control_page(pallet_page):
    pallet_page.expect_page()


def test_nav_tester_control_page(tester_page):
    tester_page.expect_page()


def test_nav_revision_page(revision_page):
    revision_page.expect_page()
