import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up WebDriver
driver = webdriver.Chrome()  # Change this to the appropriate WebDriver for your browser
wait = WebDriverWait(driver, 10)

# Test Scenario 1: Login with valid credentials
driver.get("https://www.saucedemo.com/")
username_field = driver.find_element_by_id("user-name")
password_field = driver.find_element_by_id("password")
login_button = driver.find_element_by_id("login-button")

username_field.send_keys("standard_user")
password_field.send_keys("secret_sauce")
login_button.click()

# Wait for the inventory page to load
inventory_title = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "title")))
assert inventory_title.text == "PRODUCTS"

# Test Scenario 2: Add an item to the cart and go to the cart page
add_to_cart_button = driver.find_element_by_xpath("//div[@class='inventory_item'][1]//button")
add_to_cart_button.click()

# Wait for the cart counter to update
cart_counter = wait.until(EC.text_to_be_present_in_element((By.CLASS_NAME, "shopping_cart_badge"), "1"))

# Go to the cart page
cart_link = driver.find_element_by_class_name("shopping_cart_link")
cart_link.click()

# Verify the item in the cart
item_name = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "inventory_item_name")))
assert item_name.text == "Sauce Labs Backpack"

# Test Scenario 3: Complete the checkout process
checkout_button = driver.find_element_by_xpath("//button[text()='Checkout']")
checkout_button.click()

# Fill in the checkout form
first_name = driver.find_element_by_id("first-name")
last_name = driver.find_element_by_id("last-name")
postal_code = driver.find_element_by_id("postal-code")

first_name.send_keys("John")
last_name.send_keys("Doe")
postal_code.send_keys("12345")

continue_button = driver.find_element_by_xpath("//input[@value='CONTINUE']")
continue_button.click()

# Verify the checkout summary
summary_title = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "title")))
assert summary_title.text == "CHECKOUT: OVERVIEW"

# Test Scenario 4: Complete the purchase
finish_button = driver.find_element_by_xpath("//button[text()='FINISH']")
finish_button.click()

# Verify the order confirmation
confirmation_text = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "complete-header")))
assert confirmation_text.text == "THANK YOU FOR YOUR ORDER"

# Close the browser
driver.quit()
