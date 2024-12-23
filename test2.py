from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pickle
import os
import time

# Function to log messages to a log file
def log_message(message):
    log_path = "D:/Applications/Python/Zorg_Macro/log.txt"
    with open(log_path, "a") as log_file:
        log_file.write(message + "\n")

# Set up Chrome options
options = Options()

# Profile path (adjust if necessary)
profile_path = r"C:\Users\Taffy\AppData\Local\Google\Chrome\User Data"  # Your Chrome user data path
options.add_argument(f"--user-data-dir={profile_path}")
options.add_argument("--profile-directory=Profile 1")  # Adjust to the correct profile name

# Additional arguments to bypass "not secure" issue
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-blink-features=AutomationControlled")  # Disable the automation flag
options.add_argument("--remote-debugging-port=9223")
options.add_argument("--incognito")  # Use incognito mode to prevent detection

# Set a real user-agent string to avoid detection
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")

# Optional: Add a sleep timer before starting to allow cookies/anything else to load
options.add_argument("start-maximized")  # Start maximized window

# Path to ChromeDriver
chromedriver_path = "D:/Applications/Python/chromedriver/chromedriver.exe"
driver = webdriver.Chrome(service=Service(chromedriver_path), options=options)

# Cookie file location
cookies_file = "D:/Applications/Python/Zorg_Macro/www.zorgempire.com_cookies.pkl"

try:
    # Step 1: Open Zorg Empire main page
    driver.get("https://www.zorgempire.com")
    log_message("1. Zorg Empire main page opened.")
    print("1. Zorg Empire main page opened.")

    # Step 2: Wait for and click the "Login and Play" button
    login_and_play_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//a[@class="Button Button--ghost Panel-button Button--login"]'))
    )
    login_and_play_button.click()
    log_message("2. 'Login and Play' button clicked.")
    print("2. 'Login and Play' button clicked.")

    # Step 3: Wait for and click the Google login button
    try:
        google_login_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//a[contains(@href, "/google/")]'))
        )
        google_login_button.click()
        log_message("3. Google login button clicked.")
        print("3. Google login button clicked.")
    except Exception as e:
        log_message(f"Error finding Google login button: {e}")
        print(f"Error finding Google login button: {e}")

    # Step 4: Load cookies if available
    if os.path.exists(cookies_file):
        driver.get("https://www.zorgempire.com")  # Set context for cookies
        with open(cookies_file, "rb") as cookies_pickle:
            cookies = pickle.load(cookies_pickle)
            for cookie in cookies:
                driver.add_cookie(cookie)
        driver.refresh()
        log_message("4. Cookies loaded and page refreshed.")
        print("4. Cookies loaded and page refreshed.")

    # Step 5: Verify successful login
    try:
        WebDriverWait(driver, 40).until(EC.url_contains("zorgempire.com"))
        log_message(f"5. Login successful, current URL: {driver.current_url}")
        print(f"5. Login successful, current URL: {driver.current_url}")
    except Exception as e:
        log_message(f"Error waiting for successful login: {e}")
        print(f"Error waiting for successful login: {e}")

    # Step 6: Handle dynamic content and wait for page to load completely
    try:
        WebDriverWait(driver, 20).until(
            lambda driver: driver.execute_script('return document.readyState') == 'complete'
        )
        log_message("6. JavaScript finished executing.")
        print("6. JavaScript finished executing.")
    except Exception as e:
        log_message(f"Error waiting for JavaScript to complete: {e}")
        print(f"Error waiting for JavaScript to complete: {e}")

    # Step 7: Check the page source to debug the login process
    page_source = driver.page_source
    log_message(f"Page source: {page_source[:1000]}")  # Log the first 1000 characters
    print(f"Page source: {page_source[:1000]}")  # Print the first 1000 characters for inspection

finally:
    # Close the browser after testing
    time.sleep(5)  # Delay to observe results before closing
    driver.quit()
    log_message("Browser closed.")
    print("Browser closed.")
