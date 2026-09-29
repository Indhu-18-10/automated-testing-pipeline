from selenium import webdriver
from selenium.webdriver.common.by import By


def test_successful_login():

    driver = webdriver.Chrome()

    try:
        driver.get("http://localhost:8000")

        driver.find_element(By.ID, "username").send_keys("admin")
        driver.find_element(By.ID, "password").send_keys("admin123")
        driver.find_element(By.ID, "loginButton").click()

        message = driver.find_element(By.ID, "message").text

        assert message == "Login successful"

    finally:
        driver.quit()


def test_invalid_login():

    driver = webdriver.Chrome()

    try:
        driver.get("http://localhost:8000")

        driver.find_element(By.ID, "username").send_keys("admin")
        driver.find_element(By.ID, "password").send_keys("wrong")
        driver.find_element(By.ID, "loginButton").click()

        message = driver.find_element(By.ID, "message").text

        assert message == "Invalid username or password"

    finally:
        driver.quit()