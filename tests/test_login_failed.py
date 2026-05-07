from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_login_failed(driver, base_url):
    driver.get(base_url + "/login")

    driver.find_element(By.NAME, "username").send_keys("alice")
    driver.find_element(By.NAME, "password").send_keys("alice")
    driver.find_element(By.CLASS_NAME, "login-btn").click()

    error_msg = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "error-text"))
    )

    assert "User not found" in error_msg.text