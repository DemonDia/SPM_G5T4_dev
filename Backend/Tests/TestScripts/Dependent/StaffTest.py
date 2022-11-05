from HelperFunctionForTest import *
entityName = "staff"


def getStaff():
    print("Get individual staff")
    triggerTestCase("Get staff by ID -- ID exists", True, entityName,
                    {"Staff_ID": "140001g"}, "readByStaffIDorEmail")

    triggerTestCase("Get staff by ID -- ID does not exist", False, entityName,
                    {"Staff_ID": "random"}, "readByStaffIDorEmail")

    triggerTestCase("Get staff by Email -- Email exists", True, entityName,
                    {"Email": "Derek.Tan@allinone.com.sg"}, "readByStaffIDorEmail")
    triggerTestCase("Get staff by Email -- Email does not exist", False, entityName,
                    {"Email": "anemail@allinone.com.sg"}, "readByStaffIDorEmail")

    triggerTestCase("Get staff by BOTH email and ID", False, entityName,
                    {
                        "Staff_ID": "140001g",
                        "Email": "siang-meng@live.com"
                    }, "readByStaffIDorEmail")

def testAllStaffCases():
    getStaff()