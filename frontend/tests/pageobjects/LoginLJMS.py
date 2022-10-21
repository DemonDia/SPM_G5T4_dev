from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

class LoginLJMS:
    # SEARCHBOX = (By.ID, 'lst-ib')

    def __init__(self, driver):
        self.driver = driver

    def login(self, text):
        # Find the select box
        select = Select(self.driver.find_element(By.NAME, 'cars'))

        # Select option by role text
        if (text == 'Admin'):
            select.select_by_visible_text('Admin')
        elif (text == 'User'):
            select.select_by_visible_text('User')
        elif (text == 'Manager'):
            select.select_by_visible_text('Manager')
        elif (text == 'Trainer'):
            select.select_by_visible_text('Trainer')
        else:  
            select.select_by_visible_text('Admin')
            
        # Find the button and click it
        self.driver.find_element(By.CSS_SELECTOR,'.btn-black').click()

        # Find something in homepage

    def loginWrongID(self, text):
        # Find the staff ID text box
        staffIDInput = self.driver.find_element(By.NAME, 'staffID')
        staffIDInput.clear() # Clear the text box
        staffIDInput.send_keys(text) # Enter the wrong staff ID

        # Find the button and click it
        self.driver.find_element(By.CSS_SELECTOR,'.btn-black').click()

        # Find something in homepage
        self.driver.find_element(By.CSS_SELECTOR,'.alert-danger').is_displayed()