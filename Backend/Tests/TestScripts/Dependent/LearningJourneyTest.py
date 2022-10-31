from HelperFunctionForTest import *

# ======================Test cases======================
learningJourney = "learningjourney"


def createLearningJourney():
    print("User Story: Create Learning Journey")
    triggerTestCase("Create learning journey", True, learningJourney,
                    {
                        "Staff_ID":130001,
                        "Courses": ["COR001","COR002"],
                        "Role_ID": 1
                    }, "addRelation"
                    )


def testAllLearningJourneyCases():
    createLearningJourney()