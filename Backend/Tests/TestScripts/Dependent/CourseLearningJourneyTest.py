from HelperFunctionForTest import *

# ======================Test cases======================
courselearningJourney = "courselearningjourney"


def AddCourseLearningJourney():
    print("User Story: Add course to Learning Journey")
    triggerTestCase("Create learning journey", True, courselearningJourney,
                    {
                        "LearningJourney_ID": 1,
                        "Courses": ["COR001","COR002","COR006"]
                    }, "addRelation"
                    )
def DeleteCourseLearningJourney():
    print("=============================================")
    print("User Story: Delete course from Learning Journey")
    triggerTestCase("Delete Courses from learning journey", True, courselearningJourney,
                    {
                        "LearningJourney_ID": 1,
                        "Course_ID": "COR001"
                    }, "deleteRelation"
                    )


def testAllCourseLearningJourneyCases():
    AddCourseLearningJourney()
    DeleteCourseLearningJourney()
