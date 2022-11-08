from HelperFunctionForTest import *

# ======================Test cases======================
learningjourneyskillrelation = "learningjourneyskillrelation"


def skillToLearningJourney():
    print("Add skills to learning journey")
    triggerTestCase("Both skills and learning journey exist", True, learningjourneyskillrelation,
                    {
                        "LearningJourney_ID": 1,
                        "Skills": [1, 2, 3]
                    }, "addRelation"
                    )

def testAllLearningJourneySkillRelationCases():
    skillToLearningJourney()