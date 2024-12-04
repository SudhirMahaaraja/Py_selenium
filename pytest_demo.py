import pytest
import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

def test_google_search():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(10)
    driver.get("https://google.com")
    element = driver.find_element(By.ID, "APjFqb")
    driver.find_element(By.ID, "APjFqb").send_keys("Selenium Python")
    driver.find_element(By.ID, "APjFqb").send_keys(Keys.RETURN)
    time.sleep(2)
    print(" Test Completed ")