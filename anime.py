from selenium import webdriver  # For automating the browser
from selenium.webdriver.common.by import By  # To locate elements
from sys import argv
import os  # To interact with the operating system (for file paths)
import time  # To add pauses between actions
import subprocess # To run shell commands from within the Python script


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

    # Specify the location of the IDM extension
    idm = os.path.abspath(r'F:/Extensions/idm.crx')
    options.add_extension(idm)

    # Modify the browser settings to disable images (helps speed up loading and saves bandwidth)
    prefs = {
        "profile.managed_default_content_settings.images": 2  # 2 means disable images
    }
    options.add_experimental_option("prefs", prefs)

    # Launch the Edge browser with the specified options (including extensions and settings)
    driver = webdriver.Edge(options=options)

    # Get all window handles (tabs) and switch to the main window
    main_window = driver.window_handles[1]
    driver.switch_to.window(main_window)

    # Wait for 10 seconds to ensure the extensions are fully loaded
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

    # Switch to the newly opened download window
    download_window = driver.window_handles[-1]
    driver.switch_to.window(download_window)

    # If an element isn't immediately found, the Driver will keep checking for it every 500 milliseconds for up to 10 seconds before returning an error.
    driver.implicitly_wait(10)

    # Find and extract the '1080P - mp4' download link (for high-quality video)
    Mp4_1080p = driver.find_element(By.XPATH, '//div[@class="dowload"]/a[contains(text(), "1080P - mp4")]')
    download_link = Mp4_1080p.get_attribute('href')
    driver.quit()

    return download_link


link = gogo_anime(anime=argv[1], episode_no=argv[2])
destination_folder = 'F:/Anime'

# Building the command to launch IDM to start downloading the episode from the link and save it in the destination folder
command = f'idman.exe /d "{link}" /p "{destination_folder}"'

# Running the above command in the shell from within the Python script
subprocess.run(command, shell=True)
