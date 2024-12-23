from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def login(driver, username, password):
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'username'))
    )

    username_field = driver.find_element(By.ID, "username")
    password_field = driver.find_element(By.ID, "password")
    
    username_field.send_keys(username)
    password_field.send_keys(password)
    password_field.send_keys(Keys.RETURN)
    
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'mega-1'))
    )
