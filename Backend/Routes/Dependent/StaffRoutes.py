from fastapi import Response, Depends
from Schema.IndependentSchema import Skill
from database import *
from sqlmodel import Session, select, delete, join
from config import app
from Models.DependentModels import StaffModel
from HelperFunctions import *
from fastapi import Request

# ===========================test functions===========================


@app.delete("/staff/deleteall", tags=["Staff", "DeleteAll"])
def deleteAll():
    return deleteAllData(StaffModel)


@app.post("/staff/seedall", tags=["Staff", "SeedAll"])
def addSeedData():
    return seedInitialData("staff", StaffModel, 25, False, "staff")


@app.get("/staff/one",tags=["Staff"])
async def getStaffInfo(request: Request, session: Session = Depends(get_session)):
    errors = []
    try:
        requestData = await request.json()
        if "Staff_ID" in requestData.keys():
            Staff_ID = requestData["Staff_ID"]
        else:
            Staff_ID = None
        if "Email" in requestData.keys():
            Email = requestData["Email"]
        else:
            Email = None
        getStaffInfo = None
        if Staff_ID and not Email:
            getStaffStatement = select(StaffModel).where(
                StaffModel.Staff_ID == Staff_ID)
            getStaffInfo = session.exec(getStaffStatement).all()
            getStaffInfo = getStaffInfo[0]
        elif Email and not Staff_ID:
            getStaffStatement = select(StaffModel).where(
                StaffModel.Email == Email)
            getStaffInfo = session.exec(getStaffStatement).all()
            getStaffInfo = getStaffInfo[0]
        else:
            errors.append("Choose either Staff_ID or Email!")

        if not getStaffInfo:
            errors.append("Staff not found!")

        if len(errors) > 0:
            return {
                "success": False,
                "message": errors
            }
        return {
            "success": True,
            "data": getStaffInfo
        }

    except Exception as e:
        errors.append(str(e))
        return {
            "success": False,
            "message": errors
        }
