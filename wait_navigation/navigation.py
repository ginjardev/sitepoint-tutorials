import asyncio
import re
from playwright.async_api import async_playwright, Playwright, expect, Page

# wait for load state
async def wait_state(playwright: Playwright):
    """Function `wait_state` uses wait_for_load_state() method
    to wait for navigation to given url.
    When no argument is specified, defaults to `load`.

    Args:
        playright (Playwright): playwright object
    """
    chrome = playwright.chromium
    browser = await chrome.launch()
    context = await browser.new_context()
    page = await context.new_page()
    await page.goto("https://ecommerce-playground.lambdatest.io/")

    # waits until load state wait is completed
    await page.wait_for_load_state()
    print("wait for load state completed")
    await browser.close()


# wait for url
async def wait_url(playwright: Playwright):
    """Function `wait_url` uses wait_for_url() method
    to wait for navigation to given url matching url argument.

    Args:
        playright (Playwright): playwright object
    """
    chrome = playwright.chromium
    browser = await chrome.launch()
    page = await browser.new_page()
    await page.goto("https://ecommerce-playground.lambdatest.io/")
    await page.get_by_role("link", name="Blog", exact=True).click()

    # waits for navigated url to match url argument
    await page.wait_for_url("**/blog/home")
    print("wait for URL completed")
    await browser.close()


# wait for event
async def wait_event(playwright: Playwright):
    """Function `wait_event` uses wait_for_event() method
    to wait for given event to fire.

    Args:
        playright (Playwright): playwright object
    """
    chrome = playwright.chromium
    browser = await chrome.launch()
    page = await browser.new_page()
    await page.goto(
        "https://ecommerce-playground.lambdatest.io/index.php?route=product/special"
    )
    await page.get_by_text("Continue", exact=True).click()

    # waits for event load to be completed
    await page.wait_for_event("domcontentloaded")
    print("wait for event completed")
    await browser.close()


async def wait_function(playwright: Playwright):
    """Function `wait_function` uses wait_for_function() method
    to wait until method returns when the expression returns a truthy value

    Args:
        playright (Playwright): playwright object
    """
    chrome = playwright.chromium
    browser = await chrome.launch()
    page = await browser.new_page()
    await page.goto("https://ecommerce-playground.lambdatest.io/")
    await page.get_by_role("link", name='Jolio Balia', exact=True).nth(1).click()
    await page.evaluate("() => document.title")

    # waits for function to return truthy value
    await page.wait_for_function("title = 'Jolio Balia'; () => document.title === title")
    print("wait for function completed")
    await browser.close()


async def main():
    async with async_playwright() as playwright:
        await wait_state(playwright)
        await wait_url(playwright)
        await wait_event(playwright)
        await wait_function(playwright)


asyncio.run(main())
