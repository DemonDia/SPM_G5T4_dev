from fastapi import Response, Depends
from Schema.IndependentSchema import Skill
from database import *
from sqlmodel import Session, select, delete, join
from config import app
from Models.DependentModels import LearningJourneyModel
from HelperFunctions import *
from fastapi import Request

# ===========================test functions===========================


@app.delete("/courselearningjourney/deleteall")
def deleteAll():
    return deleteAllData(LearningJourneyModel)

@app.post('/courselearningjourney/')
async def AddCourseLearningJourney(request: Request, session: Session = Depends(get_session)):
    errors = []
    try:
        requestData = await request.json()
        statement = select(LearningJourneyModel).where(
            LearningJourneyModel.LearningJourney_ID == requestData["LearningJourney_ID"])
        result = session.exec(statement)


        chosenLearningJourney = result.all()
        if len(chosenLearningJourney) == 0:
            return "testnull" # yes this returns the success = false json
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
            newCourseLearningJourneyRelation.LearningJourney_ID = requestData["LearningJourney_ID"]
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
