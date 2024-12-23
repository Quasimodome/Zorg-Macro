import os
import time
import subprocess
from selenium import webdriver
from login import login
from navigation import click_menu_item
from actions import perform_building_action

# Function to pull the latest changes from the GitHub repository
def update_repo():
    print("Pulling latest changes from GitHub...")
    subprocess.run(["git", "pull", "origin", "main"], check=True)

# Initialize WebDriver
def initialize_driver():
    driver = webdriver.Chrome(executable_path='D:/Applications/Python/chromedriver/chromedriver.exe')
    driver.get("https://yourwebsite.com")  # Replace with your website URL
    return driver

def main():
    # Update the repo to get the latest code
    update_repo()
    
    # Initialize the driver
    driver = initialize_driver()

    # Login to the website
    login(driver, "TaffyDuck121", "M5ceSw4Gfm3M5TH")

    # Navigate to the "Buildings" page
    click_menu_item(driver, 'Buildings')

    # Perform actions on the "Buildings" page
    perform_building_action(driver)

    # Wait and then close the browser
    time.sleep(5)
    driver.quit()

if __name__ == "__main__":
    main()
