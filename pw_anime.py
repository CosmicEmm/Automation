from playwright.sync_api import Playwright, sync_playwright
import time

def run(playwright: Playwright) -> None:
    # Path to the user data directory for persistent session (this is where your extensions will be saved)
    userDataDir = 'F:\\UserData\\Edge'
    
    # Path to the unpacked extension (uBlock Origin)
    extension_path = r'F:\\UserData\\Edge\uBlock Origin'

    # Launch Microsoft Edge with the specified user data directory and extension
    browser = playwright.chromium.launch_persistent_context(
        userDataDir, 
        channel='msedge',
        headless=False,
        args=[
            f"--disable-extensions-except={extension_path}",
            f"--load-extension={extension_path}"
        ]
    )
    

    page = browser.new_page()

    page.goto("https://ww19.gogoanimes.fi/")
    page.locator('[placeholder="search"]').click()
    page.locator('[placeholder="search"]').fill("haikyuu")
    page.locator('[onclick="do_search();"]').click()
    page.locator('ul > li:nth-child(1) > p.name > a').click()
    page.locator("#episode_related > li:nth-child(25) > a > div.name").click()
    page.locator("div.favorites_book > ul > li.dowloads > a").click()
    # ---------------------
    browser.close()


# Running the function
with sync_playwright() as playwright:
    run(playwright)