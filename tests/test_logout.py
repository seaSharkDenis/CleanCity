import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tests.utils import login

@pytest.mark.parametrize(
        "email, password, expected_url",
        [
            pytest.param("user@test.com", "user123", "https://cleancitytestersng.netlify.app/", id="successful_logout"), 
        ],
)
def test_logout_flow(driver, email, password, expected_url):
    # Login functionaliy
    login(driver, email, password)
    WebDriverWait(driver, 10).until(
        lambda d: "/profile" in d.current_url
    )

    driver.find_element(By.XPATH, "//button[normalize-space()='Logout']").click()
    assert expected_url == driver.current_url
