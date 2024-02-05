import re
import pytest
import asyncio
from playwright.sync_api import Page, Playwright, expect


def test_wait_load_state(page: Page):
    page.goto("https://ecommerce-playground.lambdatest.io/")
    # wait for load state wait until naviagtion is complete
    page.wait_for_load_state()
    expect(page).to_have_title("Your Store")


def test_wait_url(page: Page):
    page.goto("https://ecommerce-playground.lambdatest.io/")
    page.get_by_role("link", name="Blog", exact=True).click()
    page.wait_for_url("**/blog/home")
    expect(page).to_have_url(re.compile(".*/blog/home$"))


def test_wait_event(page: Page):
    page.goto(
        "https://ecommerce-playground.lambdatest.io/index.php?route=product/special"
    )
    page.get_by_text("Continue", exact=True).click()
    page.wait_for_event("domcontentloaded")
    expect(page).to_have_url(re.compile(".*common/home$"))


def test_wait_function(page: Page):
    page.goto("https://ecommerce-playground.lambdatest.io/")
    page.get_by_role("link", name="Jolio Balia", exact=True).nth(1).click()
    page.evaluate("() => document.title")
    page.wait_for_function(
        "title = 'Jolio Balia'; () => document.title === title"
    )
    expect(page).to_have_title("Jolio Balia")
    
