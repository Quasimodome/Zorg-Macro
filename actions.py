from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re

def extract_building_info(driver):
    """
    Extract building information (name, level, resources, and construction time)
    from the HTML table on the 'Buildings' page.
    """
    buildings_info = []

    # Wait for the table containing buildings to load
    WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.XPATH, "//table[@class='building-table']//tr"))
    )

    # Find all rows in the building table
    rows = driver.find_elements(By.XPATH, "//table[@class='building-table']//tr")

    for row in rows:
        try:
            building_name = row.find_element(By.XPATH, ".//td[2]").text
            building_level = int(re.search(r"Level (\d+)", building_name).group(1)) if "Level" in building_name else 0
            
            # Find resource details
            resources = row.find_element(By.XPATH, ".//td[3]").text
            metal = int(re.search(r"Metal: ([\d,]+)", resources).group(1).replace(",", ""))
            crystal = int(re.search(r"Crystal: ([\d,]+)", resources).group(1).replace(",", ""))
            deuterium = int(re.search(r"Deuterium: ([\d,]+)", resources).group(1).replace(",", ""))
            
            # Find construction time
            construction_time = row.find_element(By.XPATH, ".//td[4]").text.strip()

            building_info = {
                "name": building_name,
                "level": building_level,
                "metal": metal,
                "crystal": crystal,
                "deuterium": deuterium,
                "construction_time": construction_time
            }

            buildings_info.append(building_info)

        except Exception as e:
            print(f"Error extracting info for building: {e}")
    
    return buildings_info

def extract_current_resources(driver):
    """
    Extract current available resources (metal, crystal, deuterium) from the page.
    """
    current_resources = {}

    try:
        # Extract current metal, crystal, and deuterium values
        current_metal = driver.find_element(By.ID, "current_metal").text
        current_crystal = driver.find_element(By.ID, "current_crystal").text
        current_deuterium = driver.find_element(By.ID, "current_deuterium").text
        
        # Clean the values (remove the "T", "O", etc. and commas)
        current_resources['metal'] = float(re.sub(r'[^\d.]', '', current_metal))
        current_resources['crystal'] = float(re.sub(r'[^\d.]', '', current_crystal))
        current_resources['deuterium'] = float(re.sub(r'[^\d.]', '', current_deuterium))
        
    except Exception as e:
        print(f"Error extracting current resources: {e}")
    
    return current_resources

def can_upgrade_building(current_resources, building_info):
    """
    Check if the current resources are sufficient to upgrade the building.
    """
    metal_available = current_resources['metal']
    crystal_available = current_resources['crystal']
    deuterium_available = current_resources['deuterium']

    # Compare the required resources with available resources
    if (metal_available >= building_info['metal'] and
        crystal_available >= building_info['crystal'] and
        deuterium_available >= building_info['deuterium']):
        return True
    return False

def upgrade_building(driver, building_id):
    """
    Automate the building upgrade process by interacting with the building's upgrade button.
    """
    try:
        # Find the input field and button for the building upgrade
        build_input = driver.find_element(By.ID, f"build{building_id}")
        upgrade_button = driver.find_element(By.XPATH, f"//button[@type='submit'][@class='build_submit']")
        
        # Increment the building level to upgrade it
        build_input.clear()
        build_input.send_keys("1")  # Upgrade by 1 level
        upgrade_button.click()
        
    except Exception as e:
        print(f"Error upgrading building {building_id}: {e}")
