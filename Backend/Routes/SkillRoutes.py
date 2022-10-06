from fastapi import Response, Depends
from database import *
from sqlmodel import Session, select, delete
from config import app
from Models.SkillModel import SkillModel
from HelperFunctions import *


@app.delete("/skills/deleteall")
def deleteAll():
    return deleteAllData(SkillModel)


@app.post("/skills/seedall")
def addSeedData():
    return seedInitialData("skill", SkillModel)

# ===========================actual CRUD functions===========================


@app.get('/skills/')
def getSkills(session: Session = Depends(get_session)):
    stmt = select(SkillModel)
    result = session.exec(stmt).all()
    # return result
    return {
        "success": True,
        "data": result
    }


@app.post('/skills/')
def CreateSkills(skill: SkillModel, session: Session = Depends(get_session)):
    try:
        findDuplicateRoleStatement = select(SkillModel).where(SkillModel.skill_name == skill.skill_name)
        results = session.exec(findDuplicateRoleStatement)
        for duplicateRoles in results:
            return {
                "success": False,
                "message": "Skill already exists! Please try again"
            }
        if len(skill.skill_name) > 30:
            return {
                "success": False,
                "message": "Skill name exceeds character limit of 30! Please try again"
            }
        # check for description length limit
        if len(skill.skill_description) > 170:
            return {
                "success": False,
                "message": "Skill Description exceeds character limit of 170! Please try again"
            }
        session.add(skill)
        session.commit()
        session.refresh(skill)
        session.close()
        return {
            "success": True,
            "message": "Successfully added"
        }
    except Exception as e:
        return{
            "success": False,
            "message": str(e)
        }
