from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_login(driver, base_url, username, password):
    driver.get(base_url + "/login")

    driver.find_element(By.NAME, "username").send_keys(username)
    driver.find_element(By.NAME, "password").send_keys(password)
    driver.find_element(By.CLASS_NAME, "login-btn").click()

    WebDriverWait(driver, 10).until(
        EC.url_contains("farmer")
    )

    assert "farmer" in driver.current_url