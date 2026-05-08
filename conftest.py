import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

BASE_URL = "http://18.234.60.194:3000"
USERNAME = "pytest_selenium"
PASSWORD = "pytest_selenium"

@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--headless")

    # Important for Docker/Jenkins/Linux
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    # Disable notifications
    options.add_argument("--disable-notifications")

    # Disable password save popup
    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        # Disable password leak detection
        "profile.password_manager_leak_detection": False,
        "profile.default_content_setting_values.notifications": 2
    }

    options.add_experimental_option("prefs", prefs)

     # Specify the Chromium binary location (important!)
    options.binary_location = '/usr/bin/chromium'
    
    # Set custom cache path to avoid permission issues
    options.add_argument('--disk-cache-dir=/tmp/chrome-cache')

    driver = webdriver.Chrome(options=options)

    yield driver   # 👉 test runs here

    driver.quit()  # 👉 teardown


@pytest.fixture
def base_url():
    return BASE_URL

@pytest.fixture
def username():
    return USERNAME

@pytest.fixture
def password():
    return PASSWORD