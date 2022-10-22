from fastapi import Response, Depends
from Schema.DependentSchema import RoleSkillRelation
from Models.DependentModels import RoleSkillRelationModel
from database import *
from sqlmodel import Session, select, delete, join
from config import app
from Models.IndependentModels import *
from HelperFunctions import *
from fastapi import Request

# ===========================test functions===========================


@app.delete("/roleskillrelations/deleteall")
def deleteAll():
    return deleteAllData(RoleSkillRelationModel)


# ===========================actual CRUD functions===========================
# input should be an array
# requests contains "Role_ID" and a list "skills" which contains the Skill_ID of the skills to add
@app.post('/roleskillrelations/')
async def addRoleSkillRelation(request: Request, session: Session = Depends(get_session)):
    errors = []
    try:
        requestData = await request.json()
        statement = select(RoleModel).where(
            RoleModel.Role_ID == requestData["Role_ID"])
        result = session.exec(statement)
        #role = result.one()

        chosenRoleResult = result.all()
        if len(chosenRoleResult) == 0:
            return  # yes this returns the success = false json
        else:
            role = chosenRoleResult[0]
        if role == None:
            errors.append("Role does not exist!")
            errors.append(str(e))
            return {
                "success": False,
                "message": errors
            }
        for Skill_ID in requestData["Skills"]:
            newRoleSkillRelation = RoleSkillRelationModel()
            newRoleSkillRelation.Role_ID = requestData["Role_ID"]
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
            "message": "Skill(s) assigned to role"
        }

    except Exception as e:
        errors.append(str(e))
        return {
            "success": False,
            "message": errors
        }


@app.get('/roleskillrelations/{Role_ID}')
async def addRoleSkillRelation(Role_ID: int, session: Session = Depends(get_session)):
    errors = []
    try:
        role = session.get(RoleModel, Role_ID)
        if role == None:
            errors.append("Role does not exist!")
            errors.append(str(e))
            return {
                "success": False,
                "message": errors
            }
        statement = select(SkillModel.Skill_Name, SkillModel.Skill_ID).select_from(
            join(RoleModel, join(SkillModel, RoleSkillRelationModel))).where(RoleModel.Role_ID == Role_ID)
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
@app.put('/roleskillrelations/{Role_ID}')
async def updateRoleSkillRelations(Role_ID: int, request: Request, session: Session = Depends(get_session)):
    errors = []
    try:
        requestData = await request.json()
        statement = select(RoleModel).where(
            RoleModel.Role_ID == Role_ID)
        result = session.exec(statement)

        chosenRoleResult = result.all()
        if len(chosenRoleResult) == 0:
            return  # yes this returns the success = false json
        else:
            role = chosenRoleResult[0]
        if role == None:
            errors.append("Role does not exist!")
            errors.append(str(e))
            return {
                "success": False,
                "message": errors
            }

        # delete relations
        existingRoleSkillStatement = select(
            RoleSkillRelationModel).where(RoleSkillRelationModel.Role_ID == Role_ID)
        allExistingRoleSkillRelations = session.exec(
            existingRoleSkillStatement)
        allRelations = allExistingRoleSkillRelations.all()
        for relation in allRelations:
            session.delete(relation)

        # add again
        for Skill_ID in requestData["Skills"]:
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
            "message": "Related skills are updated!"
        }

    except Exception as e:
        errors.append(str(e))
        return {
            "success": False,
            "message": errors
        }
