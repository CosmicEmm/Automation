from playwright.sync_api import Playwright, sync_playwright, TimeoutError
from sys import argv
import subprocess
import logging


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def argv_check() -> bool:
    if len(argv) < 2:
        print("Please provide the name of the anime")
        exit(1)
    elif len(argv) < 3:
        print("Please provide the episode number")
        exit(1)
    elif len(argv) < 4:
        try:
            int(argv[2])
            print('Specify the browser mode: 1 for Headless; 0 for Headed')
        except ValueError:
            print("Invalid episode number. Please provide a valid integer.")
        finally:
            exit(1)
    else:
        if argv[3] not in ['0', '1']:
            print("Invalid browser mode. Use 1 for headless or 0 for headed.")
            exit()
        mode = bool(int(argv[3])) # 1 --> True; 0 --> False
    
    return mode
    

def run(
        playwright: Playwright,
        anime: str,
        episode_no: int,
        browser_mode: bool
    ) -> str:

    userDataDir = 'F:\\UserData\\Edge'
    extension_path = r'F:\\UserData\\Edge\uBlock Origin'

    browser = playwright.chromium.launch_persistent_context(
        userDataDir, channel="msedge",
        headless=browser_mode,
        args=[
            f"--disable-extensions-except={extension_path}",
            f"--load-extension={extension_path}"
        ]
    )
    
    page = browser.new_page()

    logging.info('🌐 Setting sail to the GOGOAnime website... Hold on tight!')
    page.goto("https://ww19.gogoanimes.fi/")
    logging.info('🚀 Website successfully loaded! Ready for the adventure to begin!')
    page.locator('[placeholder="search"]').click()
    logging.info("🧐 Inputting search query... Let's find that anime!")
    page.locator('[placeholder="search"]').fill(f"{anime}")
    page.locator('[onclick="do_search();"]').click()
    logging.info('🌀 Sifting through the vast animeverse...')
    logging.info('🎯 Aha! Found the one you were looking for! Great choice!🔥')
    page.locator('ul > li:nth-child(1) > p.name > a').click()
    logging.info('📜 Loading the episode list... Almost there!')
    logging.info("✅ Episode list loaded! Let’s see what we have!")
    logging.info(f"🔍 Locating episode {episode_no}... It’s got to be here somewhere!")
    page.locator(f"#episode_related > li:nth-last-child({episode_no}) > a > div.name").click()
    logging.info('🙌 Episode found! The quest continues!')
    download_url = page.locator("div.favorites_book > ul > li.dowloads > a").get_attribute('href')
    
    try:
        logging.info('⏳ Navigating to the download directory... Please wait, the treasure is almost yours!')
        page.goto(download_url)
    except TimeoutError:
        pass
    
    try:
        logging.info('🔑 Extracting the 1080P download link... The magic is happening!')
        link_element = page.locator("#content-download > div:nth-child(1) > div:nth-child(6) > a")
        href = link_element.get_attribute('href')
        logging.info('🎉 Yatta! Download link successfully extracted! You did it!')
        logging.info('🎬 Your anime adventure is about to begin! Grab your snacks! 🍿')
        logging.info('👋 Until next time, stay awesome and keep watching!')
    except TimeoutError:
        logging.error('Unable to extract the download link. Try again later!')
        return None
    
    # ---------------------
    browser.close()
    return href


mode = argv_check()

# Running the function
with sync_playwright() as playwright:
    url = run(
             playwright,
             anime=argv[1],
             episode_no=argv[2],
             browser_mode=mode
        )


if url is None:
    exit(1)
else:
    pass

destination_folder = 'F:/Anime'

idm = f'idman.exe /d "{url}" /p "{destination_folder}" /f "{argv[1]}"-EP"{argv[2]}".mp4'
subprocess.run(idm, shell=True)

