from fastapi import Response, Depends
from Schema.IndependentSchema import Skill
from database import *
from sqlmodel import Session, select, delete
from config import app
from Models.IndependentModels import SkillModel
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

@app.get('/skills/available/')
def getAvailableSkills(session: Session = Depends(get_session)):
    errors = []
    try:
        stmt = select(SkillModel).where(SkillModel.Active == 1)
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

@app.get("/skills/{Role_ID}/")
def getRole(Role_ID: int, session: Session = Depends(get_session)):
    errors = []
    try:
        role = session.get(RoleModel, Role_ID)
        # role not found
        if not role:
            errors.append("Role not found")

        if len(errors) > 0:
            return {
                "success": False,
                "message": errors
            }

        # return role
        return {
            "success": True,
            "data": role
        }
    except Exception as e:
        errors.append(str(e))
        return {
            "success": False,
            "message": errors
        }

@app.post('/skills/')
def createSkills(skill: SkillModel, session: Session = Depends(get_session)):
    errors = []
    try:
        findDuplicateRoleStatement = select(SkillModel).where(
            SkillModel.Skill_Name == skill.Skill_Name)
        results = session.exec(findDuplicateRoleStatement).one()

        # check for duplicate skill name
        if results:
            errors.append("Skill already exists! Please try again")


        # check for empty skill name
        if len(skill.Skill_Name) == 0:
            errors.append("Skill Name cannot be empty! Please try again")

        # check if skill name exceeds 30 characters
        if len(skill.Skill_Name) > 30:
            errors.append(
                "Skill Name exceeds character limit of 30! Please try again")

        # check for empty skill description
        if len(skill.Skill_Description) == 0:
            errors.append(
                "Skill Description cannot be empty! Please try again")

        # check if skill name exceeds 170 characters
        if len(skill.Skill_Description) > 170:
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
            "message": "Successfully added"
        }
    except Exception as e:
        errors.append(str(e))
        return {
            "success": False,
            "message": errors
        }

#update skill
@app.put("/skills/{Skill_ID}/")
def updateSkill(Skill_ID: int, updated_skill: SkillModel, session: Session = Depends(get_session)):
    #skill = session.get(SkillModel, Skill_ID)
    errors = []
    try:
        statement = select(SkillModel).where(SkillModel.Skill_ID == Skill_ID)
        result = session.exec(statement)
        skill = result.one()

        if skill == None:
            errors.append("Skill not found!")


            findDuplicateRoleStatement = select(SkillModel).where(
                SkillModel.Skill_Name == updated_skill.Skill_Name)
            results = session.exec(findDuplicateRoleStatement).one()

            # check for duplicate skill name
            if results:
                errors.append("Skill already exists! Please try again")


            # check for empty skill name
            if len(updated_skill.Skill_Name) == 0:
                errors.append("Skill Name cannot be empty! Please try again")

            # check if skill name exceeds 30 characters
            if len(updated_skill.Skill_Name) > 30:
                errors.append(
                    "Skill Name exceeds character limit of 30! Please try again")

            # check for empty skill description
            if len(updated_skill.Skill_Description) == 0:
                errors.append(
                    "Skill Description cannot be empty! Please try again")

            # check if skill name exceeds 170 characters
            if len(updated_skill.Skill_Description) > 170:
                errors.append(
                    "Skill Description exceeds character limit of 170! Please try again")

        if (len(errors) > 0):
            return {
                "success": False,
                "message": errors
            }

        if updated_skill.Skill_Name:
            skill.Skill_Name = updated_skill.Skill_Name
        if updated_skill.Skill_Description:
            skill.Skill_Description = updated_skill.Skill_Description

        session.add(skill)
        session.commit()
        session.refresh(skill)
        session.close()
        return {
            "success": True,
            "message": "Successfully updated"
        }
    except Exception as e:
        errors.append(str(e))
        return{
        "success":False,
        "message":errors
        }
# soft delete
@app.put("/skills/delete/{Skill_ID}/")
def softDeleteSkill(Skill_ID: int,session: Session = Depends(get_session)):
    #skill = session.get(SkillModel).where(SkillModel.Skill_Name == Skill_Name)
    statement = select(SkillModel).where(SkillModel.Skill_ID == Skill_ID)
    result = session.exec(statement)
    skill = result.one()
    if skill == None:
        return {
            "success": False,
            "message": "Skill not found "
        }
    if skill.Active:
        skill.Active = False


    session.add(skill)
    session.commit()
    session.refresh(skill)
    session.close()
    return {
        "success": True,
        "message": "Skill deleted"
    }
