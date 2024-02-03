import asyncio
from playwright.async_api import async_playwright, Playwright

# wait for load state
# async def run1(playwright: Playwright):
#     chrome = playwright.chromium
#     browser = await chrome.launch()
#     context = await browser.new_context()
#     page = await context.new_page()
#     await page.goto("https://ecommerce-playground.lambdatest.io/")
#     await page.wait_for_load_state()
#     await page.screenshot(path="screenshot.png")

#     print("Done")
#     await browser.close()


# async def main():
#     async with async_playwright() as playwright:
#         await run1(playwright)


# asyncio.run(main())


# wait for url
# async def run2(playwright: Playwright):
#     chrome = playwright.chromium
#     browser = await chrome.launch()
#     page = await browser.new_page()
#     await page.goto("https://ecommerce-playground.lambdatest.io/")
#     await page.get_by_role("link", name="Blog", exact=True).click()
#     await page.wait_for_url("**/blog/home")
#     await page.screenshot(path="screenshot.png")
#     await browser.close()


# async def main():
#     async with async_playwright() as playwright:
#         await run2(playwright)


# asyncio.run(main())


# wait for event

# async def run3(playwright: Playwright):
#     chrome = playwright.chromium
#     browser = await chrome.launch()
#     page = await browser.new_page()
#     await page.goto(
#         "https://ecommerce-playground.lambdatest.io/index.php?route=product/special"
#     )
#     await page.get_by_text("Continue", exact=True).click()
#     await page.wait_for_event("domcontentloaded")
#     await page.screenshot(path="screenshot.png")
#     print("Done")
#     await browser.close()


# async def main():
#     async with async_playwright() as playwright:
#         await run3(playwright)


# asyncio.run(main())

# wait for function


async def run4(playwright: Playwright):
    chrome = playwright.chromium
    browser = await chrome.launch()
    page = await browser.new_page()
    await page.goto("https://ecommerce-playground.lambdatest.io/")
    # await page.get_by_text("Continue", exact=True).click()
    await page.wait_for_event("load")
    await page.screenshot(path="screenshot.png")
    # buttonss = await page.get_by_role("button").all()
    # buttons = buttonss[:8]
    # # for i in buttons:
    # #     print(await i.inner_text())
    # # print("Done")
    print("Done")
    await browser.close()


async def main():
    async with async_playwright() as playwright:
        await run4(playwright)


asyncio.run(main())
