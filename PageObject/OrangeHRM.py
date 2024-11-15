"""
OrangeHRM.py contains all th methods related to OrangeHRM webpage automation

Page Object File
"""

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

# import the data and locator
from TestData.data import OrangeHRMData
from TestLocators.locators import OrangeHRMLocators

# OrangeHRMAutomation class to automate Orange HRM webpage
class OrangeHRMAutomation:

    # Create the chrome driver object
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    # start() method to launch the url
    def start(self):
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get(OrangeHRMData.url)
        return True
    
    # login() method to perform OrangeHRM Login
    def login(self):

        # Locate and enters username
        self.driver.find_element(by=By.NAME, value=OrangeHRMLocators.username_locator).send_keys(OrangeHRMData.username)
        
        # Locate and enters password
        self.driver.find_element(by=By.NAME, value=OrangeHRMLocators.password_locator).send_keys(OrangeHRMData.password)

        # Locate and click on login button
        self.driver.find_element(by=By.XPATH,value=OrangeHRMLocators.login_button_locator).click()
        return True
    
    # click_pim() method to click on PIM  button
    def click_pim(self):
        #Click on PIM
        self.driver.find_element(by=By.XPATH, value=OrangeHRMLocators.pim_button_locator).click()
        return None

    # click_add() method to click on add button
    def click_add(self):
        # Click on add
        self.driver.find_element(by=By.XPATH, value=OrangeHRMLocators.add_button_locator).click()
        return None

    # add_employee() method to add employee details
    def add_employee(self):
        
        # Enter First Name
        self.driver.find_element(by=By.NAME,value=OrangeHRMLocators.firstName_locator).send_keys(OrangeHRMData.firstname)

        # Enter Middle Name
        self.driver.find_element(by=By.NAME, value=OrangeHRMLocators.middleName_locator).send_keys(OrangeHRMData.middlename)
        
        # Enter Last Name
        self.driver.find_element(by=By.NAME, value=OrangeHRMLocators.lastName_locator).send_keys(OrangeHRMData.lastname)

        # Click on save to save the details
        self.driver.find_element(by=By.XPATH, value=OrangeHRMLocators.save_button_locator).click()
        return True
 
    # shutdown() method to quit the driver
    def shutdown(self):
        self.driver.quit()
        return None