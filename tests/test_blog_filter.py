import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from tests.utils import login

# Test Case: TC-CC-019
@pytest.mark.parametrize(
    "dropdown_value",
    [
        pytest.param("Tips", id="test_tips_filter"),
        pytest.param("Household", id="test_household_filter"),
        pytest.param("Community", id="test_community_filter"),
        pytest.param("Story", id="test_story_filter"),
        pytest.param("Recycling", id="test_recycling_filter"),
        pytest.param("Education", id="test_education_filter"),
    ],
)
def test_filter_on_posts(driver, dropdown_value):
    # Login functionaliy
    featured_posts = 2
    login(driver, email="user1@test.com", password="TestPass123")

    driver.find_element(By.XPATH, "//a[normalize-space()='Blog']").click()
    tags_element = driver.find_element(By.XPATH, "//div[@class='blog-search-filter']//select")
    tags_dropdown = Select(tags_element)
    tags_dropdown.select_by_value(dropdown_value)

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "blog-card"))
    )
    card_elements = driver.find_elements(By.CLASS_NAME, "blog-card")
    number_of_cards = len(card_elements)
    time.sleep(5)

    assert number_of_cards == featured_posts + 1

# Test Case: TC-CC-020
@pytest.mark.parametrize(
    "search_input, expected_count",
    [
        pytest.param("How CleanCity Improved My Neighborhood", 1, id="search_cleancity_blog"),
        pytest.param("Understanding Recycling Symbols", 1, id="search_recycling_blog"),
        pytest.param("5 ways to reduce household waste", 1, id="search_household_blog"),
        pytest.param("random blog post", 0, id="search_nonexistent_blog"),
    ],
)
def test_searching_posts(driver, search_input, expected_count):
    # Login functionaliy
    login(driver, email="user1@test.com", password="TestPass123")

    driver.find_element(By.XPATH, "//a[normalize-space()='Blog']").click()
    driver.find_element(By.XPATH, "//input[@placeholder='Search articles...']").send_keys(search_input)

    if expected_count > 0:
        WebDriverWait(driver, 10).until(
            lambda d: len([c for c in d.find_elements(By.XPATH, "(//div[@class='blog-card'])") if c.is_displayed()]) == expected_count
        )

        visible_cards = [c for c in driver.find_elements(By.XPATH, "(//div[@class='blog-card'])") if c.is_displayed()]
        assert len(visible_cards) == expected_count, "Expected only one result card to be visible."
