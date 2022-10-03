
from tkinter import E
from fastapi import Response, Depends
from Schema.RoleSchema import Role
from database import *
from sqlmodel import Session, select, delete
from config import app
from Models.RoleModel import RoleModel
from HelperFunctions import *
# ===========================test functions===========================


@app.delete("/roles/deleteall")
def deleteAll():
    return deleteAllData(RoleModel)


@app.post("/roles/seedall")
def addSeedData():
    return seedInitialData("role", RoleModel)


# ===========================actual CRUD functions===========================
@app.get('/roles/')
def getRoles(session: Session = Depends(get_session)):
    stmt = select(RoleModel)
    result = session.exec(stmt).all()
    for i in result:
        print(i.active)
    # return result
    return {
        "success": True,
        "data": result
    }

@app.get('/roles/available/')
def getRoles(session: Session = Depends(get_session)):
    stmt = select(RoleModel).where(RoleModel.active == 1)
    result = session.exec(stmt).all()
    # return result
    return {
        "success": True,
        "data": result
    }


@app.get("/roles/{track_id}/")
def role(track_id: int, session: Session = Depends(get_session)):
    role = session.get(RoleModel, track_id)
    if not role:
        return {
            "success": False,
            "message": "Track not found"
        }
    # return role
    return {
        "success": True,
        "data": role
    }


@app.post("/roles/")
def createRoles(role: RoleModel, session: Session = Depends(get_session)):
    try:
        # check for duplicate role name
        findDuplicateRoleStatement = select(RoleModel).where(RoleModel.role_name == role.role_name)
        results = session.exec(findDuplicateRoleStatement)
        for duplicateRoles in results:
            return {
                "success": False,
                "message": "Role already exists! Please try again"
            }

        # check for description length limit
        if len(role.role_description) > 300:
            return {
                "success": False,
                "message": "Job Description exceeds character limit of 300! Please try again"
            }

        session.add(role)
        session.commit()
        session.refresh(role)
        session.close()
        return {
            "success": True,
            "message": "Successfully added"
        }
    except Exception as e:
        return {
            "success": False,
            "message": str(e)
        }
