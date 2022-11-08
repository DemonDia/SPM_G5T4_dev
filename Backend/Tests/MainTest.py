from HelperFunctionForTest import cleanUp, seedAllData
from TestScripts.Dependent.RoleSkillRelationTest import testAllRoleSkillRelationCases
from TestScripts.Dependent.CourseSkillRelationTest import testAllCourseSkillRelationCases
from TestScripts.Independent.RoleTest import testAllRoleCases
from TestScripts.Independent.SkillTest import testAllSkillCases
from TestScripts.Dependent.LearningJourneyTest import testAllLearningJourneyCases
from TestScripts.Dependent.CourseLearningJourneyTest import testAllCourseLearningJourneyCases

def mainTest():
    # Ensures ALL existing data is wiped out to prevent inconsistencies
    cleanUp()

    # Seeds default test data
    seedAllData()

    #testAllRoleCases()
    # testAllSkillCases()
    # testAllRoleSkillRelationCases()
    #testAllCourseSkillRelationCases()
    # testAllCourseLearningJourneyCases()

    # remove all the test data after testing is complete
    #cleanUp()
    return

if __name__ == "__main__":
    mainTest()
