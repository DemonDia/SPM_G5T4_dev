from fastapi import Response, Depends
from database import *
from sqlmodel import Session, select, delete, join
from config import app
from Models.DependentModels import LearningJourneySkillRelationModel

from HelperFunctions import *
from fastapi import Request

@app.delete("/learningjourneyskillrelation/deleteall",tags=["LearningJourneySkillRelation","DeleteAll"])
def deleteAll():
    return deleteAllData(LearningJourneySkillRelationModel)


@app.post('/learningjourneyskillrelation/', tags=["LearningJourneySkillRelation"])
async def addSkillsToCourses(request: Request, session: Session = Depends(get_session)):
    errors = []
    try:
        requestData = await request.json()
        learningJourney = session.get(LearningJourneyModel, requestData["LearningJourney_ID"])
        if learningJourney == None:
            errors.append("Learning Journey does not exist!")
            return {
                "success": False,
                "message": errors
            }
        for Skill_ID in requestData["Skills"]:
            newLJSkillRelation = LearningJourneySkillRelationModel()
            newLJSkillRelation.LearningJourney_ID = requestData["LearningJourney_ID"]
            newLJSkillRelation.Skill_ID = Skill_ID
            session.add(newLJSkillRelation)

        if len(errors) > 0:
            return {
                "success": False,
                "message": errors
            }
        session.commit()
        session.close()
        return {
            "success": True,
            "message": "Skill(s) assigned to course"
        }
    except Exception as e:
        errors.append(str(e))
        return {
            "success": False,
            "message": errors
        }