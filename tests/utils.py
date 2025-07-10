from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def register(driver, full_name, email, password):
        driver.get("https://cleancitytestersng.netlify.app/")
        driver.implicitly_wait(5)
        driver.maximize_window()
        driver.find_element(By.XPATH, "//a[normalize-space()='Register']").click()
        driver.find_element(By.ID, "register-name").send_keys(full_name)
        driver.find_element(By.ID, "register-email").send_keys(email)
        driver.find_element(By.ID, "register-password").send_keys(password)
        driver.find_element(By.CLASS_NAME, "register-btn").click()

def login(driver, email, password):
    driver.get("https://cleancitytestersng.netlify.app/")
    driver.maximize_window()
    driver.find_element(By.XPATH, "//a[normalize-space()='Login']").click()
    
    # Wait for login form to appear
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "login-email")))

    driver.find_element(By.ID, "login-email").send_keys(email)
    driver.find_element(By.ID, "login-password").send_keys(password)
    driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()
