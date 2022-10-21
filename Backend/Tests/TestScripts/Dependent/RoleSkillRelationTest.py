from HelperFunctionForTest import *

# ======================Test cases======================
entityName = "roleskillrelations"


def addRoleSkillRelationTest():
    print("User Story: Assign Skill To Role")
    triggerTestCase("Both role and skill exist", True, entityName,
                    {
                        "Role_ID":8,
                        "Skills":[1,2,3]
                    }, "addRelation"
                    )


def testAllRoleSkillRelationCases():
    addRoleSkillRelationTest()
