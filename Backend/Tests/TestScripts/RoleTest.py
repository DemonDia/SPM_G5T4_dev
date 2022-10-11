from HelperFunctionForTest import *

# ======================Test cases======================
entityName = "roles"


def addDataTest():
    print("User Story: Create Roles")
    triggerTestCase("Check if HR can create new role successfully", True, entityName,
                    {
                        "role_name": "Product Manager",
                        "role_description": "Product Manager needs to collaborate effectively with cross-functional stakeholders to create a smooth user experience for job seekers and employers",
                        "active": True
                    }, "create"
                    )
    triggerTestCase("Check if error message will appear upon duplicate roles created", False, entityName,
                    {
                        "role_name": "Product Manager",
                        "role_description": "Product Manager needs to collaborate effectively with cross-functional stakeholders from Product, Design, Engineering, and Operations to create a smooth user experience for job seekers and employers",
                        "active": True
                    },"create")
    triggerTestCase("Check if error message will appear upon exceeding character limit of 300 for Job Description field", False, entityName,
                    {
                        "role_name": "Scrum Manager",
                        "role_description": "Product Manager needs to collaborate effectively with cross-functional stakeholders from Product, Design, Engineering, and Operations to create a smooth user experience for job seekers and employers. Assist the team in defining and documenting product requirements in support of development efforts. Engage customers and users actively to understand their requirements and help with product roadmap planning.",
                        "active": True
                    },"create")


def viewExistingRoleTest():
    print("User Story: View all available roles")
    print("============================================")
    beforeNoOfAllRoles = getAllRows(BASE+entityName)
    beforeNoOfAvailableRoles = getAllRows(BASE+entityName+"/available")
    print("Before:")
    print("No of all rows: "+str(len(beforeNoOfAllRoles["data"])))
    print("No of available rows: "+str(len(beforeNoOfAvailableRoles["data"])))
    addUnavailableRole = {
        "role_name": "Unavailable role",
        "role_description": "....",
        "active": False
    }
    addRow(BASE+entityName, addUnavailableRole)
    print()
    print("After:")
    afterNoOfAllRoles = getAllRows(BASE+entityName)
    afterNoOfAvailableRoles = getAllRows(BASE+entityName+"/available")
    print("No of all rows: "+str(len(afterNoOfAllRoles["data"])))
    print("No of available rows: "+str(len(afterNoOfAvailableRoles["data"])))


def testAllRoleCases():
    addDataTest()
    viewExistingRoleTest()
