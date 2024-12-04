import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Set up the WebDriver
driver = webdriver.Chrome()

# Open Google
driver.get("https://www.google.com")

# Find the search bar and enter a query
search_box = driver.find_element(By.NAME, "q")
#search_box.send_keys("Selenium Python")
search_box.send_keys(Keys.RETURN)

time.sleep(52)
# Close the browser
driver.quit()
