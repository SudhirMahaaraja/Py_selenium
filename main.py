import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Set up the WebDriver
driver = webdriver.Chrome()

# Open Google
driver.get("https://trytestingthis.netlify.app/index.html")
driver.find_element(By.NAME, "fname").send_keys("Sudhir")
driver.find_element(By.NAME, "lname").send_keys("Mahaaraja")

time.sleep(5)

driver.find_element(By.XPATH,"//button[@class='btn btn-success']").click()

time.sleep(5)
# Close the browser
driver.quit()
