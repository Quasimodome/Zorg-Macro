from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

# Specify the correct path to your ChromeDriver
chromedriver_path = r'D:/Applications/Python/chromedriver/chromedriver.exe'  # Updated path

# Create a new Chrome options object
options = Options()
options.add_argument("--start-maximized")
options.add_argument("--disable-extensions")  # Disable extensions for faster performance
#options.add_argument("--headless")  # Run Chrome in headless mode (optional, for background execution)

# Disable the use of any existing user profile
options.add_argument("--incognito")  # Run in incognito mode to avoid profile use

# Initialize the WebDriver with the specified options
driver = webdriver.Chrome(service=Service(chromedriver_path), options=options, keep_alive=True)

# Navigate to the login page
driver.get('http://corrado-game.org/login1.php?errorMessage=')

# Locate the username and password fields, and login button (adjust selectors accordingly)
username_field = driver.find_element("name", "username")
password_field = driver.find_element("name", "password")
login_button = driver.find_element("xpath", "//button[@type='submit']")

# Provide login credentials
username_field.send_keys('TaffyDuck121')
password_field.send_keys('M5ceSw4Gfm3M5TH')
login_button.click()

# Continue with other tasks once logged in...
