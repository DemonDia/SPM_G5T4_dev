import os
import sys
import unittest
import argparse

# Set path to the directory
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(CURRENT_DIR))

from pageobjects.Roles import Roles
from pageobjects.LoginPage import LoginLJMS
from driverutil.Browser import Browser





print("Current directory is: " + CURRENT_DIR)

class RunTest(unittest.TestCase):

    def setUp(self):
        localUrl = "http://localhost:8080/login"
        prodUrl = "http://spm-smallbucket.s3-website-us-east-1.amazonaws.com/login"
        self.driver.maximize_window()
        self.driver = Browser().getbrowser(browsername)
        self.driver.get(prodUrl)

        self.LoginLJMS = LoginLJMS(self.driver)
        self.Roles = Roles(self.driver)

    def test_roles(self):
        self.LoginLJMS.login("Admin")
        params = {"Role_Name": "Product Manager4", 
        "Role_Description": "Product Manager needs to collaborate effectively with cross-functional stakeholders from Product, Design, Engineering",
        "Skills": ["Scrum", "Agile methodology", "Adaptable"]}
        self.Roles.createRole(params)


    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    browser = argparse.ArgumentParser()
    browser.add_argument("-b", "--browser", required=False,
                         help="name of the browser", default="chrome")
    browser.add_argument('unittest_args', nargs='*')
    args = browser.parse_args()
    sys.argv[1:] = args.unittest_args
    browsername = vars(args)["browser"]
    unittest.main()
