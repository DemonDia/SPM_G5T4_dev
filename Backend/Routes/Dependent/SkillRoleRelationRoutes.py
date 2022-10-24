from fastapi import Response, Depends
from Schema.DependentSchema import RoleSkillRelation
from Models.DependentModels import RoleSkillRelationModel
from database import *
from sqlmodel import Session, select, delete, join
from config import app
from Models.IndependentModels import *
from HelperFunctions import *
from fastapi import Request

# ===========================actual CRUD functions===========================
# input should be an array
# requests contains "Skill_ID" and a list "skills" which contains the Role_ID of the skills to add

@app.get('/skillrolerelations/{Skill_ID}')
async def addRolesToSkill(Skill_ID: int, session: Session = Depends(get_session)):
    errors = []
    try:
        role = session.get(SkillModel, Skill_ID)
        if role == None:
            errors.append("Skill does not exist!")
            errors.append(str(e))
            return {
                "success": False,
                "message": errors
            }
        statement = select(RoleModel.Role_Name, RoleModel.Role_ID).select_from(
            join(SkillModel, join(RoleModel, RoleSkillRelationModel))).where(SkillModel.Skill_ID == Skill_ID)
        results = session.exec(statement).all()

        if len(errors) > 0:
            return {
                "success": False,
                "message": errors
            }

        return {
            "success": True,
            "data": results
        }

    except Exception as e:
        errors.append(str(e))
        return {
            "success": False,
            "message": errors
        }

# request{skills; collect skillID}
@app.put('/skillrolerelations/{Skill_ID}')
async def updateRelatedRolesOfSkill(Skill_ID: int, request: Request, session: Session = Depends(get_session)):
    errors = []
    try:
        requestData = await request.json()
        statement = select(SkillModel).where(
            SkillModel.Skill_ID == Skill_ID)
        result = session.exec(statement)

        chosenRoleResult = result.all()
        if len(chosenRoleResult) == 0:
            return  # yes this returns the success = false json
        else:
            role = chosenRoleResult[0]
        if role == None:
            errors.append("Skill does not exist!")
            errors.append(str(e))
            return {
                "success": False,
                "message": errors
            }

        # delete relations
        existingRoleSkillStatement = select(
            RoleSkillRelationModel).where(RoleSkillRelationModel.Skill_ID == Skill_ID)
        allExistingRoleSkillRelations = session.exec(
            existingRoleSkillStatement)
        allRelations = allExistingRoleSkillRelations.all()
        for relation in allRelations:
            session.delete(relation)

        # add again
        for Role_ID in requestData["Roles"]:
            newRoleSkillRelation = RoleSkillRelationModel()
            newRoleSkillRelation.Role_ID = Role_ID
            newRoleSkillRelation.Skill_ID = Skill_ID
            session.add(newRoleSkillRelation)

        if len(errors) > 0:
            return {
                "success": False,
                "message": errors
            }
        session.commit()
        session.close()
        return {
            "success": True,
            "message": "Related roles are updated!"
        }

    except Exception as e:
        errors.append(str(e))
        return {
            "success": False,
            "message": errors
        }