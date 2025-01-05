from selenium import webdriver
from selenium.webdriver.common.by import By

  
driver = webdriver.Edge()
driver.get('https://www.managingmadrid.com/')

driver.implicitly_wait(10)

fanposts_button = driver.find_element(By.CSS_SELECTOR, 'nav > ul > li > a')
link = fanposts_button.get_attribute('href')
print(link)

driver.quit

# Output: https://www.managingmadrid.com/fanposts