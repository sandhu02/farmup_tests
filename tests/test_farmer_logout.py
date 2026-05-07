from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_farmer_logout(driver, base_url, username, password):
    # 1. Login first
    driver.get(base_url + "/login")

    driver.find_element(By.NAME, "username").send_keys(username)
    driver.find_element(By.NAME, "password").send_keys(password)
    driver.find_element(By.CLASS_NAME, "login-btn").click()

    WebDriverWait(driver, 10).until(
        EC.url_contains("farmer")
    )

    assert "farmer" in driver.current_url

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