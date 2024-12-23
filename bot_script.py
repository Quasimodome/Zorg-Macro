from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set up ChromeDriver with its path
driver = webdriver.Chrome(service=Service("D:/Applications/Python/chromedriver/chromedriver.exe"))

# Open the Zorg Empire homepage
driver.get("https://www.zorgempire.com")

# Create a WebDriverWait instance to wait for elements to load
wait = WebDriverWait(driver, 10)  # Wait for up to 10 seconds

# Wait for and click the "Login and Play" button
try:
    login_and_play_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@class='Button Button--ghost Panel-button Button--login']/div/div/div[text()='Login and Play']")))
    login_and_play_button.click()
    print("Clicked 'Login and Play'.")
except Exception as e:
    print(f"Error: {e}")

# Wait for the login page to load
time.sleep(5)

# Wait for the Google login button
try:
    google_login_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/google/']/img[@alt='Login via Google Accounts']")))
    google_login_button.click()
    print("Clicked 'Login via Google'.")
except Exception as e:
    print(f"Error: {e}")

# Wait for the server selection page to load (after login)
time.sleep(5)

# Wait for the "Play Now" button for the "RELOADED" server
try:
    # Wait for the "RELOADED" server row to be visible
    reloaded_server = wait.until(EC.visibility_of_element_located((By.XPATH, "//span[text()='RELOADED']")))

    # Find the "Play Now" link for the RELOADED server
    play_now_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='RELOADED']/following-sibling::span/a[text()='PLAY NOW']")))

    # Click the "Play Now" button
    play_now_button.click()

    print("Clicked 'Play Now' for RELOADED server.")
except Exception as e:
    print(f"Error: {e}")

# Wait to ensure the page loads after clicking
time.sleep(5)

# Continue with further tasks if needed
# Optional: Close the browser after completing actions
# driver.quit()
