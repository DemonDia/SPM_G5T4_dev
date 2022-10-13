from HelperFunctionForTest import *

# ======================Test cases======================
entityName = "roleskillrelations"


def addRoleSkillRelationTest():
    print("User Story: Assign Skill To Role")
    triggerTestCase("Both role and skill exist", True, entityName,
                    {
                        "Role_ID": 1,
                        "Skill_ID": 1,
                    }, "addRelation"
                    )
    # triggerTestCase("Role does not exist", False, entityName,
    #                 {
    #                     "Role_ID": -1,
    #                     "Skill_ID": 1,
    #                 }, "addRelation")
    # triggerTestCase("Skill does not exist", False, entityName,
    #                 {
    #                     "Role_ID": 1,
    #                     "Skill_ID": -1,
    #                 }, "addRelation")
    # triggerTestCase("Both role and skill do not exist", False, entityName,
    #                 {
    #                     "Role_ID": -1,
    #                     "Skill_ID": -1,
    #                 }, "addRelation")


def testAllRoleSkillRelationCases():
    addRoleSkillRelationTest()