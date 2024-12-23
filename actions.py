from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def perform_building_action(driver):
    # Example: Wait for an element to appear and interact with it
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'building-list'))  # Replace with actual element ID
    )
    # Example: Perform an action on the "Buildings" page
    building_button = driver.find_element(By.ID, 'some-button-id')  # Replace with actual ID
    building_button.click()
