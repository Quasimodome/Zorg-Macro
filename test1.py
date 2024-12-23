import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

# Set up Chrome options (without headless mode for now)
options = Options()
options.add_argument('start-maximized')  # Maximize window at start
options.add_argument('disable-infobars')  # Disable infobars
options.add_argument('--disable-extensions')  # Disable extensions

# Specify path to chromedriver
chromedriver_path = 'D:/Applications/Python/chromedriver/chromedriver.exe'

# Initialize WebDriver
driver = webdriver.Chrome(service=Service(chromedriver_path), options=options)

# Define local file paths (replace with your repository file paths)
login_page_path = 'file:///D:/Applications/Python/Zorg_Macro/Zorg-Macro/saved_html/LoginPage.html'
buildings_page_path = 'file:///D:/Applications/Python/Zorg_Macro/Zorg-Macro/saved_html/Buildings.html'
overview_page_path = 'file:///D:/Applications/Python/Zorg_Macro/Zorg-Macro/saved_html/Overview.html'

# Load the login page
driver.get(login_page_path)

# Wait for the page to load and ensure the username and password fields are present
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "username"))
)

# Log in using credentials
username_field = driver.find_element(By.ID, "username")
password_field = driver.find_element(By.ID, "password")

# Fill in the login form
username_field.send_keys("TaffyDuck121")
password_field.send_keys("M5ceSw4Gfm3M5TH")

# Optionally, select a universe (if needed)
universe_dropdown = Select(driver.find_element(By.ID, "universe2"))
universe_dropdown.select_by_value("corrado-game.org/freya")  # Example universe

# Click the login button
login_button = driver.find_element(By.NAME, "Submit")
login_button.click()

# Wait for the page to load after login (using WebDriverWait to ensure the next page is ready)
WebDriverWait(driver, 10).until(
    EC.url_changes(login_page_path)
)

# Now load the Buildings page
driver.get(buildings_page_path)

# Wait for the Buildings page to load and ensure relevant elements are present
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "building1"))  # Example button ID
)

# Click on the first building button (adjust based on actual HTML structure)
building_button = driver.find_element(By.ID, "building1")
building_button.click()

# Wait for the action to complete (adjust based on what happens after click)
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "building-details"))  # Example class after click
)

# Now load the Overview page
driver.get(overview_page_path)

# Wait for the Overview page to load and ensure relevant elements are present
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "overview-info"))
)

# Extract information or interact with the Overview page
overview_text = driver.find_element(By.CLASS_NAME, "overview-info").text
print("Overview Info:", overview_text)

# Close the browser
driver.quit()
