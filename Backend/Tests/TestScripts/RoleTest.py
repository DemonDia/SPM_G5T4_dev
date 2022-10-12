from HelperFunctionForTest import *

# ======================Test cases======================
entityName = "roles"


def addRoleTest():
    print("User Story: Create Roles")
    triggerTestCase("Check if HR can create new role successfully", True, entityName,
                    {
                        "Role_Name": "Product Manager",
                        "Role_Description": "Product Manager needs to collaborate effectively with cross-functional stakeholders to create a smooth user experience for job seekers and employers",
                        "Active": True
                    }, "create"
                    )
    triggerTestCase("Check if error message will appear upon duplicate roles created", False, entityName,
                    {
                        "Role_Name": "Product Manager",
                        "Role_Description": "Product Manager needs to collaborate effectively with cross-functional stakeholders from Product, Design, Engineering, and Operations to create a smooth user experience for job seekers and employers",
                        "Active": True
                    },"create")
    triggerTestCase("Check if error message will appear upon exceeding character limit of 300 for Job Description field", False, entityName,
                    {
                        "Role_Name": "Scrum Manager",
                        "Role_Description": "Product Manager needs to collaborate effectively with cross-functional stakeholders from Product, Design, Engineering, and Operations to create a smooth user experience for job seekers and employers. Assist the team in defining and documenting product requirements in support of development efforts. Engage customers and users Actively to understand their requirements and help with product roadmap planning.",
                        "Active": True
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
        "Role_Name": "Unavailable role",
        "Role_Description": "....",
        "Active": False
    }
    addRow(BASE+entityName, addUnavailableRole)
    print()
    print("After:")
    afterNoOfAllRoles = getAllRows(BASE+entityName)
    afterNoOfAvailableRoles = getAllRows(BASE+entityName+"/available")
    print("No of all rows: "+str(len(afterNoOfAllRoles["data"])))
    print("No of available rows: "+str(len(afterNoOfAvailableRoles["data"])))


def testAllRoleCases():
    addRoleTest()
    viewExistingRoleTest()
