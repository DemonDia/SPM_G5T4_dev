from fastapi import Response, Depends
from Schema.IndependentSchema import Skill
from database import *
from sqlmodel import Session, select, delete, join
from config import app
from Models.DependentModels import LearningJourneyModel
from HelperFunctions import *
from fastapi import Request

# ===========================test functions===========================
@app.post("/learningjourney/seedall")
def seedAll():
    return seedInitialData("learningjourney",LearningJourneyModel,25,True)

@app.delete("/learningjourney/deleteall")
def deleteAll():
    return deleteAllData(LearningJourneyModel)


@app.post("/learningjourney/")
async def addLearningJourney(request: Request, session: Session = Depends(get_session)):
    errors = []
    try:
        requestData = await request.json()
        staffId = requestData["Staff_ID"]
        roleId = requestData["Role_ID"]

        selectedRoleStatement = select(RoleModel).where(
            RoleModel.Role_ID == roleId)
        selectedRoleStatementResult = session.exec(selectedRoleStatement)
        selectedRoleStatementResult = selectedRoleStatementResult.all()
        if (len(selectedRoleStatementResult) == 0):
            errors.append("Role does not exist")

        selectedStaffStatement = select(StaffModel).where(
            StaffModel.Staff_ID == staffId
        )
        selectedStaffStatementResult = session.exec(selectedStaffStatement)
        selectedStaffStatementResult = selectedStaffStatementResult.all()
        if (len(selectedStaffStatementResult) == 0):
            errors.append("Staff does not exist")

        if (len(errors) > 0):
            return {
                "success": False,
                "message": errors
            }
        newLearningJourney = LearningJourneyModel()
        newLearningJourney.Role_ID = roleId
        newLearningJourney.Staff_ID = staffId
        session.add(newLearningJourney)
        
        courses = requestData["Courses"]


        session.commit()
        session.close()
        return {
            "success": True,
            "message": "Learning journey created",
            "data": newLearningJourney.LearningJourney_ID
        }

    except Exception as e:
        errors.append(str(e))
        return {
            "success": False,
            "message": errors

        }
