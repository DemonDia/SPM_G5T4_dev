
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
    errors = []
    try:
        stmt = select(RoleModel)
        result = session.exec(stmt).all()
        for i in result:
            print(i.active)
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


@app.get('/roles/available/')
def getRoles(session: Session = Depends(get_session)):
    errors = []
    try:
        stmt = select(RoleModel).where(RoleModel.active == 1)
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


@app.get("/roles/{role_id}/")
def role(role_id: int, session: Session = Depends(get_session)):
    errors = []
    try:
        role = session.get(RoleModel, role_id)
        if not role:
            errors.append("Job not found")
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


@app.post("/roles/")
def createRoles(role: RoleModel, session: Session = Depends(get_session)):
    errors = []
    try:
        
        # check for duplicate role name
        findDuplicateRoleStatement = select(RoleModel).where(
            RoleModel.role_name == role.role_name)
        results = session.exec(findDuplicateRoleStatement)
        for duplicateRoles in results:
            errors.append("Job already exists! Please try again")
            break

        if len(role.role_name) == 0:
            errors.append("Job name cannot be empty! Please try again")

        if len(role.role_name) > 30:
            errors.append("Job name exceeds character limit of 30! Please try again")

        if len(role.role_name) == 0:
            errors.append(
                "Job Description cannot be empty! Please try again")

        # check for description length limit
        if len(role.role_description) > 170:
            errors.append("Job Description exceeds character limit of 170! Please try again")

        if len(errors)> 0:
            return {
                "success": False,
                "message": errors
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
