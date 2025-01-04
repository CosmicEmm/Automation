from selenium import webdriver  # For automating the browser
from selenium.webdriver.common.by import By  # To locate elements
from sys import argv
import os  # To interact with the operating system (for file paths)
import time  # To add pauses between actions


if len(argv) < 2:
    print("Please provide the name of the anime")
    exit(1)
elif len(argv) < 3:
    print("Please provide the episode number")
    exit(1)




def gogo_anime(anime, episode_no):
    # Initialize browser options for Microsoft Edge
    options = webdriver.EdgeOptions()

    # This option allows the Edge browser to stay open after the script ends
    options.add_experimental_option('detach', True)

    # Specify the location of the uBlock Origin extension (this blocks ads and unwanted content)
    ublock_origin = os.path.abspath(r'F:\Extensions\uBlock Origin.crx')
    options.add_extension(ublock_origin)

    # Modify the browser settings to disable images (helps speed up loading and saves bandwidth)
    prefs = {
        "profile.managed_default_content_settings.images": 2  # 2 means disable images
    }
    options.add_experimental_option("prefs", prefs)

    # Launch the Edge browser with the specified options (including extensions and settings)
    driver = webdriver.Edge(options=options)

    # Wait for 10 seconds to ensure the uBlock Origin extension is fully loaded
    time.sleep(10)

    # Navigate to the "GogoAnime" website
    driver.get('https://ww19.gogoanimes.fi/')

    # Find the search input box by its ID and type the name of anime
    search_box = driver.find_element(By.ID, "keyword")
    search_box.send_keys(f'{anime}')

    # Find the search button by its class name and click it to initiate the search
    search_button = driver.find_element(By.CLASS_NAME, 'btngui')
    search_button.click()

    # Wait until the search results are displayed, then click on the first result
    search_result = driver.find_element(By.CSS_SELECTOR, 'p.name a')
    search_result.click()

    # Find the episode by its pseudo-class and click on it. nth-last-child locates elements based on their position as a child of a parent, counting from the end.
    episode_button = driver.find_element(By.CSS_SELECTOR, f"#episode_related > li:nth-last-child({episode_no}) > a")
    episode_button.click()


    # Find and click the download button for the episode
    download_button = driver.find_element(By.CSS_SELECTOR, 'li.dowloads a')
    download_button.click()

    # Get all window handles (tabs) and switch to the newly opened download tab
    window_handles = driver.window_handles
    driver.switch_to.window(window_handles[-1])

    # Wait for 10 seconds to ensure the page is fully loaded
    time.sleep(10)

    # Find and click the '1080P - mp4' download link (for high-quality video)
    Mp4_1080p = driver.find_element(By.XPATH, '//div[@class="dowload"]/a[contains(text(), "1080P - mp4")]')
    Mp4_1080p.click()


gogo_anime(anime=argv[1], episode_no=argv[2])


