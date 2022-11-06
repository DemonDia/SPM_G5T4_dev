from imp import reload
from fastapi import Response, Depends
from Schema.IndependentSchema import Skill
from database import *
from sqlmodel import Session, select, delete, join
from config import app
from Models.DependentModels import LearningJourneyModel
from HelperFunctions import *
from fastapi import Request
from random import randint
# ===========================test functions===========================


@app.post("/courselearningjourney/seedall", tags=["CourseLearningJourney", "SeedAll"])
def seedAll():
    try:
        # get learning journey
        session = Session(engine)
        getLearningJourneyStatement = select(LearningJourneyModel)
        allLearningJourneys = session.exec(getLearningJourneyStatement).all()

        # get courses
        getCoursesStatement = select(CourseModel)
        allCourses = session.exec(getCoursesStatement).all()

        # create CourseLearningJourney
        for learningJourney in allLearningJourneys:
            newCourseLearningJourney = CourseLearningJourneyModel()
            newCourseLearningJourney.Course_ID = allCourses[randint(
                0, len(allCourses)-1)].Course_ID
            newCourseLearningJourney.LearningJourney_ID = learningJourney.LearningJourney_ID
            session.add(newCourseLearningJourney)
        session.commit()
        session.close()
        return {
            "success": True,
            "message": "Data is seeded"
        }
    except Exception as e:
        print(e)
        print("FAILEDDD")
        return {
            "success": False,
            "messaage": str(e)
        }


@app.delete("/courselearningjourney/deleteall", tags=["CourseLearningJourney", "DeleteAll"])
def deleteAll():
    return deleteAllData(CourseLearningJourneyModel)


@app.post('/courselearningjourney/', tags=["CourseLearningJourney"])
async def AddCourseLearningJourney(request: Request, session: Session = Depends(get_session)):
    errors = []
    try:
        requestData = await request.json()
        statement = select(LearningJourneyModel).where(
            LearningJourneyModel.LearningJourney_ID == requestData["LearningJourney_ID"])
        result = session.exec(statement)

        chosenLearningJourney = result.all()
        if len(chosenLearningJourney) == 0:
            learningJourney = None
        else:
            learningJourney = chosenLearningJourney[0]
        if learningJourney == None:
            errors.append("learningJourney does not exist!")
            errors.append(str(e))
            return {
                "success": False,
                "message": errors
            }
        for Course_ID in requestData["Courses"]:
            newCourseLearningJourneyRelation = CourseLearningJourneyModel()
            newCourseLearningJourneyRelation.LearningJourney_ID = requestData[
                "LearningJourney_ID"]
            newCourseLearningJourneyRelation.Course_ID = Course_ID
            session.add(newCourseLearningJourneyRelation)

        if len(errors) > 0:
            return {
                "success": False,
                "message": errors
            }
        session.commit()
        session.close()
        return {
            "success": True,
            "message": "Course(s) assigned to Learning Journey"
        }

    except Exception as e:
        errors.append(str(e))
        return {
            "success": False,
            "message": errors
        }


@app.delete("/courselearningjourney/", tags=["CourseLearningJourney"])
async def deleteCourseLearningJourney(request: Request, session: Session = Depends(get_session)):
    errors = []
    try:
        # find the course
        requestData = await request.json()
        selectedCourseStatement = select(CourseModel).where(
            CourseModel.Course_ID == requestData["Course_ID"])
        selectedCourse = session.exec(selectedCourseStatement).all()
        if (len(selectedCourse) == 0):
            errors.append("Course does not exist!")
        elif (len(selectedCourse) == 1):
            errors.append("Only one course left cannot delete!")
        else:
            selectedCourse = selectedCourse[0]

        # delete all the relations
        # hard delete the relations
        allRelatedRelationStatement = select(CourseLearningJourneyModel).where(
            CourseLearningJourneyModel.Course_ID == requestData["Course_ID"] and CourseLearningJourneyModel.LearningJourney_ID == requestData["LearningJourney_ID"])
        relationResults = session.exec(allRelatedRelationStatement)
        allRelations = relationResults.all()
        if len(allRelations) == 0:
            errors.append("Course not inside learning journey!")
        if len(errors) > 0:
            return {
                "success": False,
                "message": errors
            }
        for relation in allRelations:
            session.delete(relation)

        session.commit()
        session.close()
        return {
            "success": True,
            "message": "Course Learning journey deleted"
        }
    except Exception as e:
        errors.append(str(e))
        return {
            "success": False,
            "message": errors
        }
