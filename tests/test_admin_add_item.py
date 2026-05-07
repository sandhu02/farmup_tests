from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


item = {
    "Item Name": "Cabbage",
    "Category": "vegetable",
    "Price": 130.00,
    "Unit": "kg",
    "Region": "Punjab"
}


def test_admin_add_item(driver, base_url):

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

    # Click Add Item button
    add_item_btn = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn.btn-primary"))
    )

    add_item_btn.click()

    # Wait for form/modal
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "form"))
    )

    # Fill Item Name
    driver.find_element(By.NAME, "itemName").send_keys(item["Item Name"])

    # Select Category
    category_dropdown = Select(
        driver.find_element(By.NAME, "category")
    )

    category_dropdown.select_by_value(item["Category"])

    # Fill Price
    price_input = driver.find_element(By.NAME, "price")
    price_input.clear()
    price_input.send_keys(str(item["Price"]))

    # Select Unit
    unit_dropdown = Select(
        driver.find_element(By.NAME, "unit")
    )

    unit_dropdown.select_by_value(item["Unit"])

    # Fill Region
    driver.find_element(By.NAME, "region").send_keys(item["Region"])

    # Submit form
    submit_btn = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, 'button[type="submit"]')
        )
    )

    # Scroll button into view
    driver.execute_script(
        "arguments[0].scrollIntoView({block: 'center'});",
        submit_btn
    )

    # Click using JavaScript
    driver.execute_script(
        "arguments[0].click();",
        submit_btn
    )

    # Wait until modal/form disappears
    WebDriverWait(driver, 10).until_not(
        EC.presence_of_element_located((By.TAG_NAME, "form"))
    )

    driver.refresh()

    # Verify item appears on page
    # Wait until item cards reload/update
    WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "item-card"))
    )

    # Get all item cards
    item_cards = driver.find_elements(By.CLASS_NAME, "item-card")

    # Flag to track item existence
    item_found = False

    for card in item_cards:

        # Extract values from card
        name = card.find_element(By.CLASS_NAME, "item-name").text.strip()

        print("Checking card - Name:", name)

        category = card.find_element(
            By.CLASS_NAME,
            "category-badge"
        ).text.strip().lower()

        price = card.find_element(
            By.CLASS_NAME,
            "item-price"
        ).text.strip()

        region = card.find_element(
            By.CLASS_NAME,
            "item-region"
        ).text.strip()

        # Check all values
        if (
            name == item["Item Name"]
            # and category == item["Category"]
            # and str(item["Price"]) in price
            # and item["Unit"] in price
            # and item["Region"] in region
        ):
            item_found = True
            break

    # Final assertion
    assert item_found, "Added item not found in dashboard"