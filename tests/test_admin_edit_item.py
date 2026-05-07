from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

item = {
    "Item Name": "Cabbage",
    "Category": "vegetable",
    "Price": 130.00,
    "Unit": "kg",
    "Region": "Punjab"
}

def test_admin_edit_item(driver, base_url):

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

        if (
            name == item["Item Name"]
        ):
            item_found = True
            edit_card(driver, card)
            break

    if not item_found:
        raise Exception(f"Item not found: {item['Item Name']}")


def edit_card(driver, card):
    # Click Edit button
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.CLASS_NAME, "btn-edit")
        )
    )
    
    edit_btn = card.find_element(By.CLASS_NAME, "btn-edit")

    edit_btn.click()

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "form"))
    )

    # Update Price
    price_input = driver.find_element(By.NAME, "price")
    price_input.clear() 
    price_input.send_keys(str(item["Price"] + 10))  # Increase price by 10

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

    # switch to alert and accept it
    WebDriverWait(driver, 10).until(
        EC.alert_is_present()
    )
    alert = driver.switch_to.alert
    assert alert.text == "Item updated successfully!"
    alert.accept()

