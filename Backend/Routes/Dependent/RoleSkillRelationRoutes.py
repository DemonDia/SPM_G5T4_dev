from fastapi import Response, Depends
from Schema.DependentSchema import RoleSkillRelation
from Models.DependentModels import RoleSkillRelationModel
from database import *
from sqlmodel import Session, select, delete
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
        role = session.get(RoleModel, requestData["Role_ID"])
        if role == None:
            errors.append("Role does not exist!")
            errors.append(str(e))
            return {
                "success": False,
                "message": errors
            }
        for Skill_ID in requestData["skills"]:
            print("Role_ID",requestData["Role_ID"])
            print("Skill_ID",Skill_ID)
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


