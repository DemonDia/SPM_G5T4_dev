from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

class Roles:
    # SEARCHBOX = (By.ID, 'lst-ib')

    def __init__(self, driver):
        self.driver = driver

    def createRole(self):
        # Login
        select = Select(self.driver.find_element(By.NAME, 'cars'))
        select.select_by_visible_text('Admin')
        self.driver.find_element(By.CSS_SELECTOR,'.btn-black').click()
        self.driver.find_element(By.LINK_TEXT,"Roles").click()

        # click create role button
        self.driver.find_element(By.LINK_TEXT,"Create Role").click()
        self.driver.find_element(By.XPATH, "/html/body/div/div/div/div/div/form/div[1]/div[1]/div[2]/div[1]/input").send_keys("Product Manager")
        self.driver.find_element(By.XPATH, "/html/body/div/div/div/div/div/form/div[1]/div[2]/div[2]/div[1]/textarea").send_keys("Product Manager needs to collaborate effectively with cross-functional stakeholders from Product, Design, Engineering")
        self.driver.find_element(By.XPATH, "/html/body/div/div/div/div/div/div[3]/button[2]").click()
        
        # assign skills
        self.driver.find_element(By.XPATH, "/html/body/div/div/div/div/div/form/div[2]/div/div[1]/input").send_keys("Scrum")
        self.driver.find_element(By.XPATH, "/html/body/div/div/div/div/div/form/div[2]/div/div[1]/input").value