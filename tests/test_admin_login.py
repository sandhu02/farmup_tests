from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_admin_login(driver, base_url):

    driver.get(base_url + "/login")

    # Enter credentials
    driver.find_element(By.NAME, "username").send_keys("admin")
    driver.find_element(By.NAME, "password").send_keys("admin")

    # ✅ Correct checkbox click (IMPORTANT FIX)
    admin_checkbox = driver.find_element(By.ID, "role")
    if not admin_checkbox.is_selected():
        admin_checkbox.click()

    # Click login
    driver.find_element(By.CLASS_NAME, "login-btn").click()

    # Wait for redirect
    WebDriverWait(driver, 10).until(
        EC.url_contains("admin")
    )

    # Strong assertion
    assert "/admin" in driver.current_url