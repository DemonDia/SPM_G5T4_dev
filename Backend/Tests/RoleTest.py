from HelperFunctionsTest import *
BASE = "http://127.0.0.1:8000/roles/"

# ======================Test cases======================
def addDataTest():
    print("User Story: Create Roles")
    print("============================================")
    print("Check if HR can create new role successfully")
    createRolesData1 = {
        "role_name": "Product Manager",
        "role_description": "Product Manager needs to collaborate effectively with cross-functional stakeholders from Product, Design, Engineering, and Operations to create a smooth user experience for job seekers and employers",
        "active":True
        }
    createRolesResult1 = addRow(BASE, createRolesData1)
    validateOutcome(createRolesResult1, True)


    print("======================")
    print("Check if error message will appear upon duplicate roles created")
    createRolesData2 = {
        "role_name": "Product Manager",
        "role_description": "Product Manager needs to collaborate effectively with cross-functional stakeholders from Product, Design, Engineering, and Operations to create a smooth user experience for job seekers and employers",
        "active":True
    }
    createRolesResult2 = addRow(BASE, createRolesData2)
    validateOutcome(createRolesResult2, False)

    print("============================================")
    print("Check if error message will appear upon exceeding character limit of 300 for Job Description field")
    createRolesData3 = {
            "role_name": "Scrum Manager",
            "role_description": "Product Manager needs to collaborate effectively with cross-functional stakeholders from Product, Design, Engineering, and Operations to create a smooth user experience for job seekers and employers. Assist the team in defining and documenting product requirements in support of development efforts. Engage customers and users actively to understand their requirements and help with product roadmap planning.",
            "active":True
        }
    createRolesResult3 = addRow(BASE, createRolesData3)
    validateOutcome(createRolesResult3, False)


if __name__ == "__main__":
    deleteAll(BASE)
    addDataTest()
