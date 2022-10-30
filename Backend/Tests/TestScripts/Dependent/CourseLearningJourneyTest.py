from HelperFunctionForTest import *

# ======================Test cases======================
learningJourney = "courselearningjourney"


def AddCourseLearningJourney():
    print("User Story: Add course(s) to Learning Journey")
    triggerTestCase("Adding of courses to learning journey", True, learningJourney,
                    {
                        "LearningJourney_ID": 1,
                        "Courses": ["COR001","COR002","COR006"]
                    }, "addRelation"
                    )
# def DeleteCourseLearningJourney():
#     print("User Story: Delete course from Learning Journey")
#     triggerTestCase("Delete Courses from learning journey", True, learningJourney,
#                     {
#                         "LearningJourney_ID": 1,
#                         "Course_ID": "COR001"
#                     }, "deleteRelation"
#                     )


def testAllCourseLearningJourneyCases():
    AddCourseLearningJourney()
    #DeleteCourseLearningJourney()
