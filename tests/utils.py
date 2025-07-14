from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

def register(driver, full_name, email, password):
        # driver.get("https://cleancitytestersng.netlify.app")
        driver.get("https://software-testing-ten.vercel.app")
        driver.maximize_window()
        driver.implicitly_wait(5)
        driver.maximize_window()
        driver.find_element(By.XPATH, "//a[normalize-space()='Register']").click()
        driver.find_element(By.ID, "register-name").send_keys(full_name)
        driver.find_element(By.ID, "register-email").send_keys(email)
        driver.find_element(By.ID, "register-password").send_keys(password)
        driver.find_element(By.CLASS_NAME, "register-btn").click()

def login(driver, email, password):
#     driver.get("https://cleancitytestersng.netlify.app/")
    driver.get("https://software-testing-ten.vercel.app")
    driver.maximize_window()
    driver.find_element(By.XPATH, "//a[normalize-space()='Login']").click()
    
    # Wait for login form to appear
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "login-email")))

    driver.find_element(By.ID, "login-email").send_keys(email)
    driver.find_element(By.ID, "login-password").send_keys(password)
    driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()

def schedule_pickup(driver, email, full_name, pickup_location, waste_type, 
                             preferred_pickup_date, additional_description, expected_success_message):
    # Schedule pickup
    driver.find_element(By.XPATH, "//a[normalize-space()='Schedule Pickup']").click()
    driver.find_element(By.ID, "home-name").send_keys(full_name)
    driver.find_element(By.ID, "home-email").send_keys(email)
    
    pickup_location_dropdown = driver.find_element(By.ID, "home-location")
    location_select = Select(pickup_location_dropdown)
    location_select.select_by_visible_text(pickup_location)

    waste_type_dropdown = driver.find_element(By.ID, "home-waste")
    waste_select = Select(waste_type_dropdown)
    waste_select.select_by_visible_text(waste_type)

    pickup_date = driver.find_element(By.ID, "home-date")
    pickup_date.click()
    pickup_date.send_keys(preferred_pickup_date)
    driver.implicitly_wait(10)

    driver.find_element(By.ID, "home-desc").send_keys(additional_description)

    driver.find_element(By.XPATH, "//button[normalize-space()='Submit Request']").click()

    actual_success_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[@role='status']"))
    )
    actual_success_message = actual_success_element.text.strip()
    assert expected_success_message == actual_success_message
    # print(f"Expected message {expected_success_message}")
    # print(f"Actual message {actual_success_message}")
    # driver.implicitly_wait(10)