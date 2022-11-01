from HelperFunctionForTest import *

# ======================Test cases======================
learningJourney = "learningjourney"


def createLearningJourney():
    print("User Story: Create Learning Journey")
    triggerTestCase("Create learning journey", True, learningJourney,
                    {
                        "Staff_ID": 130001,
                        "Courses": ["COR001", "COR002"],
                        "Role_ID": 1
                    }, "addRelation"
                    )


def viewLearningJourney():
    print("View Learning Journey")
    triggerTestCase("View all learning journeys", True, learningJourney,
                    None, "readAll")
    triggerTestCase("View learning journey by ID --Exists", True, learningJourney,
                    None, "readById", 1)

    triggerTestCase("View learning journey by ID --Does not exist", False, learningJourney,
                    None, "readById", -1)

    triggerTestCase("View learning journey by Staff ID --Staff exists", True, learningJourney,
                    None, "readByStaffId", 130001)
    triggerTestCase("View learning journey by Staff ID --Staff does not exist", False, learningJourney,
                    None, "readByStaffId", -1)


def testAllLearningJourneyCases():
    createLearningJourney()
    viewLearningJourney()
