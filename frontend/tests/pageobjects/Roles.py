from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Roles:
    # SEARCHBOX = (By.ID, 'lst-ib')

    def __init__(self, driver):
        self.driver = driver

    def createRole(self):
        self.driver.maximize_window()
        # Login
        select = Select(self.driver.find_element(By.NAME, 'cars'))
        select.select_by_visible_text('Admin')
        self.driver.find_element(By.CSS_SELECTOR,'.btn-black').click()
        self.driver.find_element(By.LINK_TEXT,"Roles").click()

        # click create role button
        element = self.driver.find_element(By.LINK_TEXT, "Roles")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        self.driver.find_element(By.LINK_TEXT, "Roles").click()
        self.driver.find_element(By.LINK_TEXT, "Create Role").click()
        self.driver.find_element(By.CSS_SELECTOR, ".row:nth-child(1) .form-control").click()
        self.driver.find_element(By.CSS_SELECTOR, ".row:nth-child(1) .form-control").send_keys("Product Manager")
        self.driver.find_element(By.CSS_SELECTOR, ".row:nth-child(2) .form-control").click()
        self.driver.find_element(By.CSS_SELECTOR, ".row:nth-child(2) .form-control").send_keys("Product Manager needs to collaborate effectively with cross-functional stakeholders from Product, Design, Engineering")

        element = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//button[text()='Next: Assign Skills']")))
        element.location_once_scrolled_into_view
        # self.driver.find_element(By.XPATH, "/html/body/div[@id='app']/div/div/div[@id='createRoleMain']/div[@class='col-sm-12 col-xl-8 mx-auto my-3 p-5 text-start rounded rounded-4 shadow-lg mb-5 bg-body']/div[@class='row d-flex justify-content-around my-sm-3 my-md-5 p-3']/button[@class='btn col-md-4 col-sm-5 m-2 order-sm-last order-first btn-primary']").click()
        # continuebtn = WebDriverWait(self.driver, 10).until (EC.presence_of_element_located((By.XPATH, "/html/body/div[@id='app']/div/div/div[@id='createRoleMain']/div[@class='col-sm-12 col-xl-8 mx-auto my-3 p-5 text-start rounded rounded-4 shadow-lg mb-5 bg-body']/div[@class='row d-flex justify-content-around my-sm-3 my-md-5 p-3']/button[@class='btn col-md-4 col-sm-5 m-2 order-sm-last order-first btn-primary' and not(@disabled)]")))
        # continuebtn.click()
        element.click()

        self.driver.find_element(By.NAME, "pillSearch").click()
        self.driver.find_element(By.NAME, "pillSearch").send_keys("Scrum")
        self.driver.find_element(By.CSS_SELECTOR, ".autocomplete-box > li").click()
        self.driver.find_element(By.NAME, "pillSearch").click()
        self.driver.find_element(By.NAME, "pillSearch").send_keys("Agile methodology")
        self.driver.find_element(By.CSS_SELECTOR, ".autocomplete-box > li").click()
        self.driver.find_element(By.NAME, "pillSearch").click()
        self.driver.find_element(By.NAME, "pillSearch").send_keys("Adaptable")
        self.driver.find_element(By.CSS_SELECTOR, ".autocomplete-box > li").click()


        self.driver.find_element(By.ID, "nextButton").click()
        self.driver.find_element(By.ID, "nextButton").click()
        self.driver.find_element(By.CSS_SELECTOR, ".btn-secondary").click()