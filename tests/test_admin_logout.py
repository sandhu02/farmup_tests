from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_admin_logout(driver, base_url, username, password):
    # Open login page
    driver.get(base_url + "/login")

    # Login as admin
    driver.find_element(By.NAME, "username").send_keys("admin")
    driver.find_element(By.NAME, "password").send_keys("admin")

    # Click admin checkbox
    admin_checkbox = driver.find_element(By.ID, "role")

    if not admin_checkbox.is_selected():
        admin_checkbox.click()

    # Click login
    driver.find_element(By.CLASS_NAME, "login-btn").click()

    # Wait for admin dashboard
    WebDriverWait(driver, 10).until(
        EC.url_contains("admin")
    )

    assert "/admin" in driver.current_url

    # 2. Click logout button
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "btn-logout"))
    )
    
    driver.find_element(By.CLASS_NAME, "btn-logout").click()

    # 3. Verify we are back on the login page
    WebDriverWait(driver, 10).until(
        EC.url_contains("/login")
    )

    assert "/login" in driver.current_url