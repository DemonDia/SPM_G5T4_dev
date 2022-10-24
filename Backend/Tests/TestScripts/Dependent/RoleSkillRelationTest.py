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

def updateSkillsOfRole():
    print("Update skills of role")
    triggerTestCase("Update skills of role,", True, skillToRole,
                    {
                        "Skills": [10,11,12]
                    }, "updateById",2
                    )

def updateRolesToSkill():
    print("Update roles of skill")
    triggerTestCase("Update roles of skill", True, roleToSkill,
                    {
                        "Roles": [10, 11, 12]
                    }, "updateById",2
                    )


def viewSkillsRelatedToRole():
    print("View skills related to role")
    triggerTestCase("View skills related to role", True, skillToRole,
                    None, "readById", 1)


def viewRolesRelatedToSkill():
    print("View roles related to skill")
    triggerTestCase("View roles related to skill", True, roleToSkill,
                    None, "readById", 1)




def testAllRoleSkillRelationCases():
    addRoleSkillRelationTest()
    addSkillsToRoleTest()
    viewSkillsRelatedToRole()
    viewRolesRelatedToSkill()
    updateSkillsOfRole()
    updateRolesToSkill()
    
