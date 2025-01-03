from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os
import time

options = webdriver.EdgeOptions()
options.add_experimental_option('detach', True)
ublock_origin = os.path.abspath(r'F:\Extensions\uBlock Origin.crx')
options.add_extension(ublock_origin)
prefs = {
    "profile.managed_default_content_settings.images": 2  # 2 means disable images
}
options.add_experimental_option("prefs", prefs)
driver = webdriver.Edge(options=options)
time.sleep(10)
driver.get('https://ww19.gogoanimes.fi/')
search_box = driver.find_element(By.ID, "keyword")
search_box.send_keys('Fullmetal Alchemist Brotherhood')
search_button = driver.find_element(By.CLASS_NAME, 'btngui')
search_button.click()
search_result = driver.find_element(By.LINK_TEXT, 'Fullmetal Alchemist: Brotherhood')
search_result.click()
episode = driver.find_element(By.XPATH, '//a[@href=" /fullmetal-alchemist-brotherhood-episode-5"]')
episode.click()
download_button = driver.find_element(By.CSS_SELECTOR, 'li.dowloads a')
download_button.click()
window_handles = driver.window_handles
driver.switch_to.window(window_handles[-1])
print(driver.current_url)
time.sleep(10)
Mp4_1080p = driver.find_element(By.XPATH, '//div[@class="dowload"]/a[contains(text(), "1080P - mp4")]')
Mp4_1080p.click()