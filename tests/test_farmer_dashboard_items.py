from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_farmer_dashboard_items(driver, base_url, username, password):

    # Open login page
    driver.get(base_url + "/login")

    # Login
    driver.find_element(By.NAME, "username").send_keys(username)
    driver.find_element(By.NAME, "password").send_keys(password)
    driver.find_element(By.CLASS_NAME, "login-btn").click()

    # Wait for farmer dashboard
    WebDriverWait(driver, 10).until(
        EC.url_contains("farmer")
    )

    # Wait until item cards load
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "item-card"))
    )

    # Click first item card
    cards = driver.find_elements(By.CLASS_NAME, "item-card")

    assert len(cards) > 0

    cards[0].click()

    # Wait for item detail page
    WebDriverWait(driver, 10).until(
        EC.url_contains("itemDetail")
    )

    # Verify navigation
    assert "itemDetail" in driver.current_url