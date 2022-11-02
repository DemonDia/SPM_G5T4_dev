from imp import reload
from fastapi import Response, Depends
from database import *
from sqlmodel import Session, select, delete, join
from config import app
from Models.DependentModels import CourseLearningJourneyModel
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

        if not learningJourney:
            errors.append("learningJourney does not exist!")
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
