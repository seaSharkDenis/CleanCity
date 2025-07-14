import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tests.utils import login

# Test Case TC-CC-010
@pytest.mark.parametrize(
        "email, password, expected_url",
        [
            pytest.param("user@test.com", "user123", "https://software-testing-ten.vercel.app/profile", id="session_persist"), 
        ],
)
def test_session_persistence(driver, email, password, expected_url):
    # Login functionaliy
    login(driver, email, password)
    WebDriverWait(driver, 10).until(
        lambda d: "/profile" in d.current_url
    )
    driver.refresh()
    driver.implicitly_wait(5)
    assert expected_url == driver.current_url

# Test Case TC-CC-011
@pytest.mark.parametrize(
        "email, password, expected_url",
        [
            pytest.param("user@test.com", "user123", "https://software-testing-ten.vercel.app/", id="session_cleared_affter_logout"), 
        ],
)
def test_session_clearance_after_logout(driver, email, password, expected_url):
    # Login functionaliy
    login(driver, email, password)
    WebDriverWait(driver, 10).until(
        lambda d: "/profile" in d.current_url
    )

    driver.find_element(By.XPATH, "//button[normalize-space()='Logout']").click()
    assert expected_url == driver.current_url

    driver.find_element(By.XPATH, "//a[normalize-space()='Feedback']").click()
    expected_text = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH,"//*[contains(text(), 'Sign In') or contains(text(), 'Login')]",))
    )
    assert expected_text.is_displayed()