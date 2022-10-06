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
    errors = []
    try:
        stmt = select(SkillModel)
        result = session.exec(stmt).all()
        # return result
        return {
            "success": True,
            "data": result
        }
    except Exception as e:
        errors.append(str(e))
        return {
            "success": False,
            "message": errors
        }


@app.post('/skills/')
def CreateSkills(skill: SkillModel, session: Session = Depends(get_session)):
    errors = []
    try:
        findDuplicateRoleStatement = select(SkillModel).where(
            SkillModel.skill_name == skill.skill_name)
        results = session.exec(findDuplicateRoleStatement)
        for duplicateRoles in results:
            errors.append("Skill already exists! Please try again")
            break

        if len(skill.skill_name) == 0:
            errors.append("Skill name cannot be empty! Please try again")

        if len(skill.skill_name) > 30:
            errors.append(
                "Skill name exceeds character limit of 30! Please try again")

        if len(skill.skill_description) == 0:
            errors.append(
                "Skill Description cannot be empty! Please try again")

        if len(skill.skill_description) > 170:
            errors.append(
                "Skill Description exceeds character limit of 170! Please try again")

        if (len(errors) > 0):
            return {
                "success": False,
                "message": errors
            }
        session.add(skill)
        session.commit()
        session.refresh(skill)
        session.close()
        return {
            "success": True,
            "message": "Skill have been added"
        }
    except Exception as e:
        errors.append(str(e))
        return {
            "success": False,
            "message": errors
        }
