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
    return


def testAllSkillCases():
    addSkillTest()
    viewExistingSkillTest()
