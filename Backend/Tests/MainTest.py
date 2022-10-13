from HelperFunctionForTest import cleanUp, seedAllData
from TestScripts.RoleTest import testAllRoleCases
from TestScripts.SkillTest import testAllSkillCases
from TestScripts.RoleSkillRelationTest import testAllRoleSkillRelationCases
def mainTest():
    # Ensures ALL existing data is wiped out to prevent inconsistencies
    cleanUp()

    # Seeds default test data
    seedAllData()

    # trigger test cases for each entity
    testAllRoleCases()
    testAllSkillCases()
    testAllRoleSkillRelationCases()

    # remove all the test data after testing is complete
    cleanUp()
    return

if __name__ == "__main__":
    mainTest()
