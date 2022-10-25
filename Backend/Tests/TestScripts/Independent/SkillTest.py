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
    beforeNoOfAllSkills = getAllRows(BASE+entityName+"/")
    beforeNoOfAvailableSkills=getAllRows(BASE+entityName+"/available/")  #get all skills where active=1
    print("Before")
    print("No of all rows: "+str(len(beforeNoOfAllSkills["data"])))
    print("No of available rows: "+str(len(beforeNoOfAvailableSkills["data"])))
    triggerTestCase("View Existing Skills",
                    True, entityName+"/available/", {}, "readAll", None)

    afterNoOfAllSkills=getAllRows(BASE+entityName+"/")
    afterNoOfAvailableSkills = getAllRows(BASE+entityName+"/available/")
    print("After")
    print("No of all rows: "+str(len(afterNoOfAllSkills["data"])))
    print("No of available rows: "+str(len(afterNoOfAvailableSkills["data"])))
    return

def updatingSkillTest():
    print("User Story: Update Skill")
    triggerTestCase("Update skill fields",
                    True, entityName, {
                        "Skill_Name": "Fluffing",
                        "Skill_Description": "Thinking on the spot",
                        "Active": True
                    }, "updateById", 1)
    return

#do it
def deleteSkillTest():
    print("User Story: Soft Delete Skill")
    beforeNoOfAllSkills = getAllRows(BASE+entityName+"/")
    beforeNoOfAvailableSkills=getAllRows(BASE+entityName+"/available/")  #get all skills where active=1
    print("Before")
    print("No of all rows: "+str(len(beforeNoOfAllSkills["data"])))
    print("No of available rows: "+str(len(beforeNoOfAvailableSkills["data"])))
    triggerTestCase("soft Delete skill fields",
                    True, entityName, {
                    }, "softDelete", 1)
    afterNoOfAllSkills=getAllRows(BASE+entityName+"/")
    afterNoOfAvailableSkills = getAllRows(BASE+entityName+"/available/")
    print("After")
    print("No of all rows: "+str(len(afterNoOfAllSkills["data"])))
    print("No of available rows: "+str(len(afterNoOfAvailableSkills["data"])))
    return

def testAllSkillCases():
    addSkillTest()
    viewExistingSkillTest()
    updatingSkillTest()
    deleteSkillTest()
