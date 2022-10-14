
from fastapi import Response, Depends
from database import *
from sqlmodel import Session, select, delete
from config import app
from Models.IndependentModels import RoleModel
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
def getAvailableRoles(session: Session = Depends(get_session)):
    errors = []
    try:
        stmt = select(RoleModel).where(RoleModel.Active == 1)
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


@app.get("/roles/{Role_ID}/")
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


@app.post("/roles/")
def createRoles(role: RoleModel, session: Session = Depends(get_session)):
    errors = []
    try:

        # check for duplicate role name
        findDuplicateRoleStatement = select(RoleModel).where(
            RoleModel.Role_Name == role.Role_Name)
        results = session.exec(findDuplicateRoleStatement)
        for duplicateRoles in results:
            errors.append("Role already exists! Please try again")
            break
        # empty role name
        if len(role.Role_Name) == 0:
            errors.append("Role Name cannot be empty! Please try again")

        # role name longer than 30 characters
        if len(role.Role_Name) > 30:
            errors.append("Role Name exceeds character limit of 30! Please try again")

        # role description is empty
        if len(role.Role_Description) == 0:
            errors.append(
                "Role Description cannot be empty! Please try again")

        # role description longer than 170 characters
        if len(role.Role_Description) > 170:
            errors.append("Role Description exceeds character limit of 170! Please try again")

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
