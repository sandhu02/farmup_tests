from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_farmer_advice_exists(driver, base_url, username, password):

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

    # Wait for advice container to load
    advice_container = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "advice-container"))
    )

    # Get advice text
    advice_text = advice_container.text

    # Verify advice section exists
    assert advice_container.is_displayed()

    # Verify heading exists
    assert "Remember" in advice_text

    # Verify actual advice text exists
    assert len(advice_text.strip()) > 0
