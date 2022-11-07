from HelperFunctionForTest import cleanUp, seedAllData
from TestScripts.Dependent.RoleSkillRelationTest import testAllRoleSkillRelationCases
from TestScripts.Dependent.CourseSkillRelationTest import testAllCourseSkillRelationCases
from TestScripts.Independent.RoleTest import testAllRoleCases
from TestScripts.Independent.SkillTest import testAllSkillCases
from TestScripts.Dependent.StaffTest import testAllStaffCases
from TestScripts.Dependent.LearningJourneyTest import testAllLearningJourneyCases
from TestScripts.Dependent.CourseLearningJourneyTest import testAllCourseLearningJourneyCases
from TestScripts.Dependent.LearningJourneySkillTest import testAllLearningJourneySkillRelationCases
import pytest

@pytest.fixture(autouse=True)
def start():
    cleanUp()
    seedAllData()
    yield
    # cleanUp()


def mainTest():
    # trigger test cases for each entity
    testAllRoleCases()
    testAllSkillCases()
    testAllRoleSkillRelationCases()
    testAllCourseSkillRelationCases()
    testAllLearningJourneyCases()
    testAllCourseLearningJourneyCases()
    testAllLearningJourneySkillRelationCases()
    # remove all the test data after testing is complete

if __name__ == "__main__":
    cleanUp()
    seedAllData()
    # mainTest()
    # cleanUp()
