import time
import pytest
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tests.utils import login
from tests.utils import schedule_pickup


# Test Case TC-CC-011
@pytest.mark.parametrize(
    "email, password",
    [
        pytest.param("user1@test.com", "TestPass123", id="request_increment_check_upon_creation")
    ],
)
def test_profile_activity_on_requests(driver, email, password):
    # Login functionaliy
    login(driver, email, password)

    # Request pickup
    schedule_pickup(driver, email, full_name="John Doe", pickup_location="Nairobi", waste_type="General Waste",
                     preferred_pickup_date="20072025", additional_description="Please ring the bell",
                       expected_success_message="Your waste pickup request has been submitted!")
    
    # check if request is added
    driver.find_element(By.XPATH, "//a[normalize-space()='Profile']").click()

    driver.find_element(By.XPATH, "//button[normalize-space()='My Requests']").click()

    
    driver.find_element(By.XPATH, "//a[normalize-space()='Feedback']").click()
    expected_text = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH,"//*[contains(text(), '20/07/2025') or contains(text(), 'Waste')]",))
    )
    assert expected_text.is_displayed()


# Test Case TC-CC-021
@pytest.mark.parametrize(
    "email, password, expected_url",
    [
        pytest.param("user1@test.com", "TestPass123", "https://software-testing-ten.vercel.app/profile", id="profile_viewing")
    ],
)
def test_profile_viewing(driver, email, password, expected_url):
    # Login functionaliy
    login(driver, email, password)

    assert driver.current_url == expected_url
    email_text = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH,f"//*[contains(text(), '{email}')]",))
    )
    email_text.is_displayed()


# Test Case TC-CC-022
@pytest.mark.parametrize(
    "parameter, new_value, should_update",
    [
        pytest.param("Email", "johndoe@gmail.com", True, id="editing_profile_with_valid_email"),
        pytest.param("Email", "user2.com", False, id="editing_profile_with_invalid_email"),
        pytest.param("Name", "John Due", True, id="editing_profile_with_name"),
        pytest.param("Name", "", False, id="editing_profile_with_empty_name"),
        pytest.param("Email", "",False, id="editing_profile_with_empty_email"),
    ],
)
def test_profile_editing(driver, parameter, new_value, should_update, 
                         email="user1@test.com", password="pass123"):
    # Login functionaliy
    login(driver, email, password)

    driver.find_element(By.XPATH, "//button[normalize-space()='Edit Profile']").click()
    input_element = driver.find_element(By.XPATH, f"//input[@placeholder='{parameter}']")
    input_element.clear()
    input_element.send_keys(new_value)

    driver.find_element(By.XPATH, "//button[normalize-space()='Save']").click()
    
    if should_update:
        expected_result = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, f"//*[contains(text(), '{new_value}')]",))
        )
        assert expected_result.is_displayed()
    else:
        error_element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'invalid') or contains(@class, 'error')]"))
        )
        assert error_element.is_displayed()
