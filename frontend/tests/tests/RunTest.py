import unittest
import argparse
import os, sys

# Set path to the directory 
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(CURRENT_DIR))

from driverutil.Browser import Browser
from pageobjects.LoginLJMS import LoginLJMS


class RunTest(unittest.TestCase):

    def setUp(self):
        localUrl = "http://localhost:8080/login"
        prodUrl = "http://spm-smallbucket.s3-website-us-east-1.amazonaws.com/login"

        self.driver = Browser().getbrowser(browsername)
        self.driver.get(localUrl)
        self.LoginLJMS = LoginLJMS(self.driver)

    def testLogin(self):
        self.LoginLJMS.login("Admin") 

    def testLoginWrongID(self):
        self.LoginLJMS.loginWrongID("190001")

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
