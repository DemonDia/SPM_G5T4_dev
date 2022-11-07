from HelperFunctionForTest import *

# ======================Test cases======================
learningjourneyskillrelation = "learningjourneyskillrelation"


def skillToLearningJourney():
    print("Add skills to learning journey")
    triggerTestCase("Both skills and learning journey exist", True, learningjourneyskillrelation,
                    {
                        "Role_ID": 8,
                        "Skills": [1, 2, 3]
                    }, "addRelation"
                    )

def testAllLearningJourneySkillRelationCases():
    skillToLearningJourney()