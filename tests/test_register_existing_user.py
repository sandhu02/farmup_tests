from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_register_existing_user(driver, base_url):
    driver.get(base_url + "/register")

    driver.find_element(By.NAME, "name").send_keys("John Doe")
    driver.find_element(By.NAME, "username").send_keys("johndoe")  # already exists
    driver.find_element(By.NAME, "password").send_keys("johndoe")
    driver.find_element(By.CLASS_NAME, "login-btn").click()

    error_msg = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "error-text"))
    )

    assert "User already exists" in error_msg.text