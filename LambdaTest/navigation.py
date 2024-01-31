# import asyncio

# from playwright.async_api import async_playwright, Playwright


# async def main():
#     async with async_playwright() as p:
#         browser = await p.chromium.launch()
#         page = await browser.new_page()
#         await page.goto("https://playwright.dev/")  # Waits for load event
#         # Now you can interact with elements on the page
#         await page.screenshot(path="screenshot.png")
#         html = await page.content()
#         print(html)


# asyncio.run(main())


import asyncio
from playwright.async_api import async_playwright, Playwright


async def run(playwright: Playwright):
    chrome = playwright.chromium
    browser = await chrome.launch()
    context = await browser.new_context()
    page = await context.new_page()
    await page.goto("https://techchale.com")
    await page.screenshot(path="screenshot.png")
    html = await page.content()
    print(html)
    await browser.close()


async def main():
    async with async_playwright() as playwright:
        await run(playwright)


asyncio.run(main())
