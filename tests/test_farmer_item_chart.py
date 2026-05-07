from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_farmer_item_chart(driver, base_url, username, password):

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


    # Wait until page loads
    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CLASS_NAME, "item-detail-container"))
    )

    # ✅ Verify item title exists
    title = driver.find_element(By.CLASS_NAME, "item-detail-title")

    assert title.is_displayed()

    # ✅ Verify chart canvas exists
    chart = driver.find_element(By.TAG_NAME, "canvas")

    assert chart.is_displayed()

    # ✅ Verify section title
    section_title = driver.find_element(By.CLASS_NAME, "section-title")

    assert "Price History" in section_title.text

    # ✅ Verify stat cards exist
    stat_cards = driver.find_elements(By.CLASS_NAME, "stat-card")

    assert len(stat_cards) == 3

    # ✅ Verify back button works
    back_btn = driver.find_element(By.CLASS_NAME, "back-button")

    assert back_btn.is_displayed()

    back_btn.click()

    # Example redirect assertion
    WebDriverWait(driver, 10).until(
        EC.url_contains("farmer")
    )

    assert "farmer" in driver.current_url