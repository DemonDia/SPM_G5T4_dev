from fastapi import Response, Depends
from Schema.RoleSkillRelationSchema import RoleSkillRelation
from database import *
from sqlmodel import Session, select, delete
from config import app
from Models.IndependentModels import *
from HelperFunctions import *
# ===========================test functions===========================


# ===========================actual CRUD functions===========================
@app.post('/roleskillrelations/')
def addRoleSkillRelation(roleSkillRelation: RoleSkillRelation, session: Session = Depends(get_session)):
    errors = []
    try:
        # put None as default; declare within the function
        # role = None
        # skill = None
        # if(roleSkillRelation.Role_ID == None):
        #     errors.append("Role is not selected")

        # else:
        #     role = session.get(RoleModel, roleSkillRelation.Role_ID)

        # if(roleSkillRelation.Skill_ID == None):
        #     errors.append("Skill is not selected")
        # else:

        role = session.get(RoleModel, roleSkillRelation.Role_ID)
        skill = session.get(SkillModel, roleSkillRelation.Skill_ID)
        if role == None:
            errors.append("Role does not exist!")
        if skill == None:
            errors.append("Skill does not exist")
        if len(errors > 0):
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
