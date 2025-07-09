import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_login_success():
    driver = webdriver.Chrome()
    try:
        driver.get("https://cleancitytestersng.netlify.app/")
        driver.implicitly_wait(5)
        driver.find_element(By.XPATH, "//a[normalize-space()='Login']").click()
        driver.implicitly_wait(2)
        driver.find_element(By.ID, "login-email").send_keys("user@test.com")
        driver.find_element(By.ID, "login-password").send_keys("user123")
        driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()
        driver.implicitly_wait(5)
        assert driver.current_url == "https://cleancitytestersng.netlify.app/profile"
    finally:
        # Close driver
        driver.quit


def register_success():
    driver = webdriver.Chrome()
    try:
        driver.get("https://cleancitytestersng.netlify.app/")
        driver.implicitly_wait(5)
        driver.find_element(By.XPATH, "//a[normalize-space()='Register']").click()
        driver.find_element(By.ID, "register-name").send_keys("User1")
        driver.find_element(By.ID, "register-email").send_keys("user1@test.com")
        driver.find_element(By.ID, "register-password").send_keys("Pass123")
        driver.find_element(By.CLASS_NAME, "register-btn").click()
        assert driver.current_url == "https://cleancitytestersng.netlify.app/login"
    finally:
       driver.quit  
