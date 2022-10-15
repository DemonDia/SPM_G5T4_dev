from fastapi import Response, Depends
from Models.DependentModels import RoleSkillRelationModel
from database import *
from sqlmodel import Session, select, delete
from config import app
from Models.IndependentModels import *
from HelperFunctions import *
# ===========================test functions===========================


@app.delete("/roleskillrelations/deleteall")
def deleteAll():
    return deleteAllData(RoleSkillRelationModel)


# ===========================actual CRUD functions===========================
@app.post('/roleskillrelations/')
def addRoleSkillRelation(roleSkillRelation: RoleSkillRelationModel, session: Session = Depends(get_session)):
    errors = []
    try:
        print("roleSkillRelation", roleSkillRelation)
        print("roleSkillRelation", roleSkillRelation.Role_ID)
        print("roleSkillRelation", roleSkillRelation.Skill_ID)
        role = session.get(RoleModel, roleSkillRelation.Role_ID)
        skill = session.get(SkillModel, roleSkillRelation.Skill_ID)
        if role == None:
            errors.append("Role does not exist!")
        if skill == None:
            errors.append("Skill does not exist")
        if len(errors) > 0:
            return {
                "success": False,
                "message": errors
            }
        session.add(roleSkillRelation)
        session.commit()
        session.refresh(roleSkillRelation)
        session.close()
        return {
            "success": True,
            "message": "Skill assigned to role"
        }
    except Exception as e:
        errors.append(str(e))
        return {
            "success": False,
            "message": errors
        }
