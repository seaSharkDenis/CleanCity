import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tests.utils import login

# Zephyr Test Case: TC-CC-018
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
    login(driver, email, password)
    assert expected_url == driver.current_url


# Zephyr Test Case: TC-CC-006,
@pytest.mark.parametrize(
        "input_email, input_password, expected_url",
        [
            pytest.param("usre@tset.com", "TestPass", "https://cleancitytestersng.netlify.app/login", id="invalid_email_stays_on_login"),
            pytest.param("user@test.com", "test123", "https://cleancitytestersng.netlify.app/login",id="invalid_password_stays_on_login"),
        ],
)
def test_login_with_invalid_credentials(driver, input_email, input_password, expected_url):
    login(driver, input_email, input_password)

    error = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'wrong password') or contains(text(), 'wrong email')]"))
    )
    assert error.is_displayed()
    assert expected_url == driver.current_url