from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_farmer_location_exists(driver, base_url, username, password):

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

    # Wait for header actions section
    header_actions = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "header-actions"))
    )

    # Get all paragraph tags inside header
    location_element = header_actions.find_element(By.TAG_NAME, "p")

    # Extract location text
    location_text = location_element.text
    print("Location text:", location_text)

    # Verify location element is visible
    assert location_element.is_displayed()

    driver.find_element(By.CLASS_NAME, "btn-logout").click()

    # WebDriverWait(driver, 10).until(
    #     lambda d: "📍" in location_element.text and len(location_element.text.replace("📍", "").strip()) > 0
    # )

    # assert location_text.__contains__("📍 ")

    # # Extract text after pin + space
    # city_name = location_text.replace("📍 ", "").strip()

    # # Verify city name exists
    # assert len(city_name) > 0
