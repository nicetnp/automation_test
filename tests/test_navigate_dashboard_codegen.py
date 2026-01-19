import re
from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    page.goto("http://10.216.128.98/")
    page.get_by_role("link", name="📊Dashboard").click()
    expect(page.get_by_role("heading", name="Failures Dashboard")).to_be_visible()
    page.get_by_role("link", name="🔬Calibration").click()
    expect(page.get_by_role("heading", name="Calibration Management")).to_be_visible()
    page.get_by_role("link", name="📦Pallet Control").click()
    expect(page.get_by_role("heading", name="PM Pallet Management")).to_be_visible()
    page.goto("http://10.216.128.98/block-tester")
    expect(page.get_by_role("heading", name="Blocked Testers")).to_be_visible()
    page.get_by_role("link", name="📈CPK").click()
    expect(page.get_by_role("heading", name="SPC & Process Capability")).to_be_visible()
    page.get_by_role("link", name="📈Revision Control").click()
    expect(page.get_by_role("heading", name="Program Revision Control")).to_be_visible()