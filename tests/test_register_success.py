from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_register_success(driver, base_url):
    driver.get(base_url + "/register")

    driver.find_element(By.NAME, "name").send_keys("John Doe")
    driver.find_element(By.NAME, "username").send_keys("johndoe")  
    driver.find_element(By.NAME, "password").send_keys("johndoe")
    driver.find_element(By.CLASS_NAME, "login-btn").click()

    success_msg = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "success-text"))
    )

    assert "Registration successful" in success_msg.text