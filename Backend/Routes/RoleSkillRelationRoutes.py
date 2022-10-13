from fastapi import Response, Depends
from Schema.RoleSkillRelationSchema import RoleSkillRelation
from database import *
from sqlmodel import Session, select, delete
from config import app
from Models.RoleModel import RoleModel
from HelperFunctions import *
# ===========================test functions===========================


# ===========================actual CRUD functions===========================
@app.post('/roleskilllink/')
def getRoles(session: Session = Depends(get_session)):
    errors = []
    return
    try:
        stmt = select(RoleModel)
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


