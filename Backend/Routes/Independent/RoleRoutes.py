
from fastapi import Response, Depends
from database import *
from sqlmodel import Session, select, delete, join
from config import app
from Models.IndependentModels import RoleModel, SkillModel
from Models.DependentModels import RoleSkillRelationModel
from HelperFunctions import *

# ===========================test functions===========================


@app.delete("/roles/deleteall")
def deleteAll():
    return deleteAllData(RoleModel)


@app.post("/roles/seedall")
def addSeedData():
    return seedInitialData("role", RoleModel)

# ===========================helper functions===========================


def getRelatedSkills(targetModelIdValue):
    try:
        session = Session(engine)
        statement = select(SkillModel.Skill_ID,SkillModel.Skill_Name).select_from(join(SkillModel, RoleSkillRelationModel)).where(
            RoleSkillRelationModel.Role_ID == targetModelIdValue)
        results = session.exec(statement).all()
        return {
            "success": True,
            "data": results
        }
    except Exception as e:
        return {
            "success": False,
            "messaage": e,
            "data": []
        }
# returns json


def getAllRelatedSkills():
    try:
        skillDict = {}
        session = Session(engine)
        statement = select(SkillModel.Skill_Name, RoleModel.Role_ID).select_from(
            join(RoleModel, join(SkillModel, RoleSkillRelationModel)))
        results = session.exec(statement).all()
        for result in results:
            if (result.Role_ID not in skillDict.keys()):
                skillDict[result.Role_ID] = [result.Skill_Name]
            else:
                skillDict[result.Role_ID].append(result.Skill_Name)
        return {
            "success": True,
            "data": skillDict
        }
    except Exception as e:
        return {
            "success": False,
            "message": e,
            "data": []
        }
# ===========================actual CRUD functions===========================


@app.get('/roles/')
def getRoles(session: Session = Depends(get_session)):
    errors = []
    try:
        stmt = select(RoleModel)
        getAllRoles = session.exec(stmt).all()
        allSkills = getAllRelatedSkills()["data"]
        allRoles = []
        for role in getAllRoles:
            roleDict = {}
            for columnName, columnValue in role:
                roleDict[columnName] = columnValue
                if role.Role_ID in allSkills.keys():

                    roleDict["Skills"] = allSkills[role.Role_ID]
                else:
                    roleDict["Skills"] = []
            allRoles.append(roleDict)
        return {
            "success": True,
            "data": allRoles,
        }
    except Exception as e:
        print(e)
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
        availableRoles = session.exec(stmt).all()
        allSkills = getAllRelatedSkills()["data"]
        allRoles = []
        for role in availableRoles:
            roleDict = {}
            for columnName, columnValue in role:
                roleDict[columnName] = columnValue
                if role.Role_ID in allSkills.keys():

                    roleDict["Skills"] = allSkills[role.Role_ID]
                else:
                    roleDict["Skills"] = []
            allRoles.append(roleDict)
        return {
            "success": True,
            "data": allRoles,
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
        roleDict = {}
        for columnName, columnValue in role:
            roleDict[columnName] = columnValue
        outcome = getRelatedSkills(role.Role_ID)
        roleDict["Skills"] = outcome["data"]
        # return role
        return {
            "success": True,
            "data": roleDict
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
            errors.append(
                "Role Name exceeds character limit of 30! Please try again")

        # role description is empty
        if len(role.Role_Description) == 0:
            errors.append(
                "Role Description cannot be empty! Please try again")

        # role description longer than 170 characters
        if len(role.Role_Description) > 170:
            errors.append(
                "Role Description exceeds character limit of 170! Please try again")

        if len(errors) > 0:
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
            "message": "Successfully added",
            "data":role.Role_ID
        }

    except Exception as e:
        return {
            "success": False,
            "message": str(e)
        }

# update role


@app.put("/roles/{Role_ID}/")
def updateRole(Role_ID: int, updated_role: RoleModel, session: Session = Depends(get_session)):
    errors = []
    try:
        #skill = session.get(SkillModel, Skill_ID)
        statement = select(RoleModel).where(RoleModel.Role_ID == Role_ID)
        result = session.exec(statement)
        role = result.one()

        if role == None:
            errors.append("Role not found!")

        findDuplicateRoleStatement = select(RoleModel).where(
            RoleModel.Role_Name == updated_role.Role_Name and RoleModel.Role_ID != Role_ID)
        results = session.exec(findDuplicateRoleStatement).all()
        print("Results",results)

        # check for duplicate skill name
        if len(results)>0:
            errors.append("Role already exists! Please try again")

        # check for empty skill name
        if len(updated_role.Role_Name) == 0:
            errors.append("Role Name cannot be empty! Please try again")

        # check if skill name exceeds 30 characters
        if len(updated_role.Role_Name) > 30:
            errors.append(
                "Role Name exceeds character limit of 30! Please try again")

        # check for empty skill description
        if len(updated_role.Role_Description) == 0:
            errors.append(
                "Role Description cannot be empty! Please try again")

        # check if skill name exceeds 170 characters
        if len(updated_role.Role_Description) > 170:
            errors.append(
                "Role Description exceeds character limit of 170! Please try again")

        if (len(errors) > 0):
            return {
                "success": False,
                "message": errors
            }
        if updated_role.Role_Name:
            role.Role_Name = updated_role.Role_Name
        if updated_role.Role_Description:
            role.Role_Description = updated_role.Role_Description

        session.add(role)
        session.commit()
        session.refresh(role)
        session.close()
        return {
            "success": True,
            "message": "Successfully updated"
        }
    except Exception as e:
        errors.append(str(e))
        return {
            "success": False,
            "message": errors
        }

# softDeleteRole


@app.put("/roles/delete/{Role_ID}/")
def softDeleteRole(Role_ID: int, session: Session = Depends(get_session)):
    try:
        #skill = session.get(SkillModel).where(SkillModel.Skill_Name == Skill_Name)
        statement = select(RoleModel).where(RoleModel.Role_ID == Role_ID)
        result = session.exec(statement)
        role = result.one()
        if role == None:
            return {
                "success": False,
                "message": "Role not found "
            }
        if role.Active:
            role.Active = False

        # hard delete the relations
        allRelatedRelationStatement = select(RoleSkillRelationModel).where(
            RoleSkillRelationModel.Role_ID == Role_ID)
        relationResults = session.exec(allRelatedRelationStatement)
        allRelations = relationResults.all()
        for relation in allRelations:
            session.delete(relation)

        session.add(role)
        session.commit()
        session.refresh(role)
        session.close()
        return {
            "success": True,
            "message": "Role deleted"
        }
    except Exception as e:
        return {
            "success": False,
            "message": str(e)
        }
