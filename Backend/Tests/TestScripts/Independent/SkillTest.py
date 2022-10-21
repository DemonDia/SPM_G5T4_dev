from HelperFunctionForTest import *

# ======================Test cases======================
entityName = "skills"


def addSkillTest():
    print("User Story: Create Skills")
    triggerTestCase("Check if HR can create new skill successfully", True, entityName, {
        "Skill_Name": "Leadership",
        "Skill_Description": "“Strengths and abilities individuals demonstrate that help to oversee processes, guide initiatives and steer their employees toward the achievement of goals.",
        "Active": True
    }, "create")

    triggerTestCase("Check if error message will appear upon duplicate skills created", False, entityName, {
        "Skill_Name": "Leadership",
        "Skill_Description": "Analytical skills in data science to visualise data",
        "Active": True
    }, "create")

    triggerTestCase("Check if error message will appear upon exceeding character limit of 30 for Skill Name field", False, entityName, {
        "Skill_Name": "Teamworkkkkkkkkkkkkkkkkkkkkkkkk",
        "Skill_Description": "Working with people from different places",
        "Active": True
    }, "create")
    return


def viewExistingSkillTest():
    print("User Story: View Existing Skills")
    before = getSingleRow(BASE+entityName+"/available/", 1)
    print("before",before)
    triggerTestCase("View Existing Skills",
                    True, entityName, {
                    }, "readAllAvailable", None)
    after = getSingleRow(BASE+entityName, 1)
    print("after",after)
    return

def updatingSkillTest():
    print("User Story: Update Skill")
    #before = getSingleRow(BASE+entityName, 1)
    #print("before",before)
    triggerTestCase("Update skill fields",
                    True, entityName, {
                        "Skill_Name": "Fluffing",
                        "Skill_Description": "Thinking on the spot",
                        "Active": True
                    }, "updateById", 1)
    #after = getSingleRow(BASE+entityName, 1)
    #print("after",after)
    return

def testAllSkillCases():
    addSkillTest()
    viewExistingSkillTest()
    updatingSkillTest()
