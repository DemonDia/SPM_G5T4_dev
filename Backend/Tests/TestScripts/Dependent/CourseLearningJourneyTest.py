from HelperFunctionForTest import *
import requests
from random import randint
# ======================Test cases======================
courselearningJourney = "courselearningjourney"


def AddCourseLearningJourney():
    print("User Story: Add course to Learning Journey")
    triggerTestCase("Create learning journey", True, courselearningJourney,
                    {
                        "LearningJourney_ID": 1,
                        "Courses": ["COR001", "COR002", "COR006"]
                    }, "addRelation"
                    )


def DeleteCourseLearningJourney():
    print("=============================================")
    print("User Story: Delete course from Learning Journey")
    triggerTestCase("Delete Courses from learning journey - only one course left", False, courselearningJourney,
                    {
                        "LearningJourney_ID": 1,
                        "Course_ID": "COR001"
                    }, "deleteRelation"
                    )
    getCoursesResponse = requests.get(BASE+"course")
    allCourses = getCoursesResponse.json()
    coursesToAdd = []
    for course in allCourses["data"]:
        coursesToAdd.append(course["Course_ID"])
    addedRow = requests.post(BASE+"learningjourney/", json={
        "Staff_ID": 130001,
        "Courses": coursesToAdd,
        "Role_ID": 21
    })
    addedRowJson = addedRow.json()
    triggerTestCase("Delete Courses from learning journey - more than one course left", False, courselearningJourney,
                    {
                        "LearningJourney_ID": addedRowJson["data"],
                        "Course_ID": coursesToAdd[randint(1, 5)]
                    }, "deleteRelation"
                    )


def testAllCourseLearningJourneyCases():
    AddCourseLearningJourney()
    DeleteCourseLearningJourney()


if __name__ == "__main__":
    testAllCourseLearningJourneyCases()