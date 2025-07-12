import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tests.utils import login
from selenium.webdriver.support.ui import Select

@pytest.mark.parametrize(
    "email, password, expected_url, full_name, " \
    "pickup_location, waste_type, preferred_pickup_date, additional_description," \
    " expected_success_message",
    [
        pytest.param("user1@test.com", "TestPass123",  "https://cleancitytestersng.netlify.app/profile", 
                     "John Doe", "Nairobi", "General Waste", "20072025", "Please ring the bell", 
                     "Your waste pickup request has been submitted!", id="request_increment_check_upon_creation")
    ],
)
def test_request_persistence(driver, email, password, expected_url, full_name, pickup_location, waste_type, 
                             preferred_pickup_date, additional_description, expected_success_message):
    # Login
    login(driver, email, password)
    assert expected_url == driver.current_url

    # fetch request before creation of new request
    driver.find_element(By.XPATH, "//a[normalize-space()='Dashboard']").click()
    request_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[@aria-label='Dashboard Analytics']//div[1]//span[2]"))
    )
    WebDriverWait(driver, 10).until(lambda d: request_element.text.strip() != '')
    request_value = int(request_element.text.strip())

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

    driver.find_element(By.XPATH, "//a[normalize-space()='Dashboard']").click()
    updated_request_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[@aria-label='Dashboard Analytics']//div[1]//span[2]"))
    )
    WebDriverWait(driver, 10).until(lambda d: updated_request_element.text.strip() != '')
    new_request_value = int(updated_request_element.text.strip())
    assert new_request_value == request_value + 1