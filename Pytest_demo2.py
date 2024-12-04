import pytest
import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture()
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(10)
    #Yield the WebDriver instance
    yield driver
    #Close the WebDriver instance
    driver.quit()


def test_google_search(driver):
    driver.get("https://google.com")
    element = driver.find_element(By.ID, "APjFqb")
    driver.find_element(By.ID, "APjFqb").send_keys("Selenium Python")
    driver.find_element(By.ID, "APjFqb").send_keys(Keys.RETURN)
    time.sleep(2)
    print(" Test Completed ")