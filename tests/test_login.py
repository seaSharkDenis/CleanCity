import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tests.utils import login

@pytest.mark.parametrize(
        "email, password, expected_url",
        [
            pytest.param("usertest.com", "user123", "https://cleancitytestersng.netlify.app/login", id="invalid_email_stays_on_login"),
            pytest.param("user@test.com", "user123", "https://cleancitytestersng.netlify.app/profile",id="valid_login_redirects_to_profile"),
        ],
)
def test_login_flow(driver, email, password, expected_url):
    """
    Tests the login functionality wih various email/password combinations
    and asserts the resuling URL.
    """
    driver.get("https://cleancitytestersng.netlify.app/")

    driver.find_element(By.XPATH, "//a[normalize-space()='Login']").click()
    
    # Wait for login form to appear
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "login-email")))

    driver.find_element(By.ID, "login-email").send_keys(email)
    driver.find_element(By.ID, "login-password").send_keys(password)
    driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()
    assert expected_url == driver.current_url


