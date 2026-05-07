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


def test_admin_delete_item(driver, base_url):

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
            delete_card(driver, card)
            break

    if not item_found:
        raise Exception(f"Item not found: {item['Item Name']}")


def delete_card(driver, card):
    # Click Delete button on first item card
    delete_btn = card.find_element(By.CLASS_NAME, "btn-delete")

    delete_btn.click()

    # Wait for browser confirmation alert
    WebDriverWait(driver, 10).until(
        EC.alert_is_present()
    )

    # Switch to alert
    alert = driver.switch_to.alert

    # Optional: verify alert text
    if (alert.text != "Are you sure you want to delete this item?"):
        raise Exception(f"Unexpected alert text: {alert.text}")
    else:
        # Click OK
        alert.accept()

    WebDriverWait(driver, 10).until(
        EC.alert_is_present()
    )

    # Switch to second alert
    alert = driver.switch_to.alert
    assert alert.text == "Item deleted successfully!"
    alert.accept()



    