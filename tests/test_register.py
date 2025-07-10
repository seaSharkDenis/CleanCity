import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tests.utils import register


@pytest.mark.parametrize(
    "full_name, email, password, expected_url",
    [
        pytest.param(
            "John Doe",
            "user@test.com",
            "TestPass123",
            "https://cleancitytestersng.netlify.app/login",
            id="valid_registration_redirects_to_login",
        ),
        pytest.param(
            "",
            "user@test.com",
            "TestPass123",
            "https://cleancitytestersng.netlify.app/register",
            id="ommiting_name_stays_on_register",
        ),
        pytest.param(
            "John Doe",
            "",
            "TestPass123",
            "https://cleancitytestersng.netlify.app/register",
            id="ommiting_email_stays_on_register",
        ),
        pytest.param(
            "John Doe",
            "user@test.com",
            "",
            "https://cleancitytestersng.netlify.app/register",
            id="ommiting_password_stays_on_register",
        ),
    ],
)
def test_register_success(driver, full_name, email, password, expected_url):

    driver.get("https://cleancitytestersng.netlify.app/")
    driver.maximize_window()
    driver.implicitly_wait(5)
    driver.find_element(By.XPATH, "//a[normalize-space()='Register']").click()
    driver.find_element(By.ID, "register-name").send_keys(full_name)
    driver.find_element(By.ID, "register-email").send_keys(email)
    driver.find_element(By.ID, "register-password").send_keys(password)
    driver.find_element(By.CLASS_NAME, "register-btn").click()
    assert driver.current_url == expected_url
    driver.implicitly_wait(5)


@pytest.mark.parametrize(
    "full_name, email, password, expected_success",
    [
        pytest.param(
            "John Doe",
            "user@test.com",
            "TestPass",
            True,
            id="password_with_eight_characters",
        ),
        pytest.param(
            "John Doe",
            "user@test.com",
            "TestPass1",
            True,
            id="password_with_nine_characters",
        ),
        pytest.param(
            "John Doe",
            "user@Test.com",
            "Test",
            False,
            id="password_with_four_characters",
        ),
        pytest.param(
            "John Doe",
            "user@Tes.com",
            "TestPas",
            False,
            id="password_witth_seven_characters",
        ),
    ],
)
def test_password_length(driver, full_name, email, password, expected_success):
    driver.get("https://cleancitytestersng.netlify.app/")
    driver.maximize_window()
    driver.implicitly_wait(5)

    driver.find_element(By.XPATH, "//a[normalize-space()='Register']").click()
    driver.find_element(By.ID, "register-name").send_keys(full_name)
    driver.find_element(By.ID, "register-email").send_keys(email)
    driver.find_element(By.ID, "register-password").send_keys(password)
    driver.find_element(By.CLASS_NAME, "register-btn").click()


    if expected_success:
        WebDriverWait(driver, 5).until(lambda d: "/login" in d.current_url)
        assert driver.current_url == "https://cleancitytestersng.netlify.app/login"
    else:
        WebDriverWait(driver, 5).until(lambda d: "/register" in d.current_url)
        assert driver.current_url == "https://cleancitytestersng.netlify.app/register"
        
        error = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located(
                (By.XPATH, "//*[contains(text(), 'minimum') or contains(text(), 'invalid') or contains(text(), 'password')]")
            )
        )
        assert error.is_displayed()

def test_cannot_register_same_email_twice(driver):
    email = "user@test.com"
    password = "TestPass123"
    name = "John Doe"

    # First registration
    register(driver, name, email, password)

    WebDriverWait(driver, 10).until(
        lambda d: "/login" in d.current_url or "/profile" in d.current_url
    )

    # Second registration attempt
    register(driver, name, email, password)

    error = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "//*[contains(text(), 'already exists') or contains(text(), 'taken') or contains(text(), 'used')]",
            )
        )
    )
    assert error.is_displayed()
