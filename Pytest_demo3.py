import  pytest
import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManage, ChromeDriverManager


@pytest.fixture()
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(10)
    #Yield the WebDriver instance
    yield driver
    #Close the WebDriver instance
    driver.quit()

@pytest.mark.parametrize("username, password", [
    ("test", "test"),
    ("test", "test"),
    ("test", "test"),
])

def test_login(driver, username, password):
    driver.get("https://trytestingthis.netlify.app/")
    username_field = driver.find_element(By.ID, "uname")
    password_field = driver.find_element(By.ID, "pwd")
    submit_button = driver.find_element(By.XPATH, "//input[@value='Login']")

    username_field.send_keys(username)
    password_field.send_keys(password)
    time.sleep(20)
    submit_button.click()
    assert "Successful" in driver.page_source