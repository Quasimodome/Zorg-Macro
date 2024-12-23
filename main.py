import time
from selenium import webdriver
from login import login
from navigation import click_menu_item
from actions import extract_building_info, extract_current_resources, can_upgrade_building, upgrade_building

def initialize_driver():
    driver = webdriver.Chrome(executable_path='D:/Applications/Python/chromedriver/chromedriver.exe')
    driver.get("http://corrado-game.org/login1.php")
    return driver

def main():
    # Initialize the driver
    driver = initialize_driver()

    # Login to the website
    login(driver, "TaffyDuck121", "M5ceSw4Gfm3M5TH")

    # Navigate to the "Buildings" page
    click_menu_item(driver, 'Buildings')

    # Extract building information
    buildings_info = extract_building_info(driver)

    # Extract current resources
    current_resources = extract_current_resources(driver)

    # Print extracted building info and current resources (for debugging purposes)
    print("Current Resources:", current_resources)
    for building in buildings_info:
        print(f"Building: {building['name']}, Level: {building['level']}, "
              f"Metal: {building['metal']}, Crystal: {building['crystal']}, "
              f"Deuterium: {building['deuterium']}, Time: {building['construction_time']}")

    # Example: Check and upgrade a specific building (e.g., building ID 1)
    building_id = 1
    building_info = buildings_info[building_id - 1]  # Get building info (index is 0-based)
    
    if can_upgrade_building(current_resources, building_info):
        print(f"Upgrading {building_info['name']}...")
        upgrade_building(driver, building_id)
    else:
        print(f"Not enough resources to upgrade {building_info['name']}.")

    # Wait and then close the browser
    time.sleep(5)
    driver.quit()

if __name__ == "__main__":
    main()
