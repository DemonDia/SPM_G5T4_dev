from HelperFunctionForTest import *

# ======================Test cases======================
roleToSkill = "skillrolerelations"
skillToRole = "roleskillrelations"


def addRoleSkillRelationTest():
    print("User Story: Assign Skill To Role")
    triggerTestCase("Both role and skill exist", True, skillToRole,
                    {
                        "Role_ID": 8,
                        "Skills": [1, 2, 3]
                    }, "addRelation"
                    )


def addSkillsToRoleTest():
    print("Add roles to skill")
    triggerTestCase("Add roles to skills", True, roleToSkill,
                    {
                        "Skill_ID": 1,
                        "Roles": [1, 2, 3]
                    }, "addRelation")

def viewSkillsRelatedToRole():
    print("View skills related to role")
    triggerTestCase("View skills related to role", True, skillToRole,
                    None, "readById",1)

def viewRolesRelatedToSkill():
    print("View roles related to skill")
    triggerTestCase("View roles related to skill", True, skillToRole,
                    None, "readById",1)

def testAllRoleSkillRelationCases():
    addRoleSkillRelationTest()
    addSkillsToRoleTest()
    viewSkillsRelatedToRole()
