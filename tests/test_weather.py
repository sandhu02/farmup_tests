from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_weather(driver, base_url, username, password):

    # 1. Open login page
    driver.get(base_url + "/login")

    # 2. Login
    driver.find_element(By.NAME, "username").send_keys(username)
    driver.find_element(By.NAME, "password").send_keys(password)
    driver.find_element(By.CLASS_NAME, "login-btn").click()

    # 3. Wait for farmer dashboard
    WebDriverWait(driver, 10).until(
        EC.url_contains("farmer")
    )

    # 4. Open Weather Page
    weather_btn = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "btn-secondary"))
    )

    weather_btn.click()

    WebDriverWait(driver, 10).until(
        EC.url_contains("checkWeather")
    )

    # 5. Enter city name
    city_input = driver.find_element(By.CLASS_NAME, "city-input")
    city_input.clear()
    city_input.send_keys("sahiwal")

    # 6. Click Search button (IMPORTANT missing step)
    driver.find_element(By.CLASS_NAME, "search-btn").click()

    # 7. Wait for weather data to load
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "current-weather-card"))
    )

    # 8. Assertions (core validations)

    # Location check
    location = driver.find_element(By.TAG_NAME, "h2").text
    assert len(location.strip()) > 0

    # Temperature check
    temp = driver.find_element(By.CLASS_NAME, "current-temp").text
    assert "°C" in temp

    # Weather condition check
    condition = driver.find_element(By.CLASS_NAME, "weather-condition").text
    assert len(condition.strip()) > 0

    # Forecast check (5 days)
    forecast_days = driver.find_elements(By.CLASS_NAME, "forecast-day")
    assert len(forecast_days) == 5

    # Hourly forecast check
    hourly_items = driver.find_elements(By.CLASS_NAME, "hourly-item")
    assert len(hourly_items) > 0