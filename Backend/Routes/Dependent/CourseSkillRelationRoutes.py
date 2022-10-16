from fastapi import Response, Depends, Request
from Models.DependentModels import CourseSkillRelationModel
from database import *
from sqlmodel import Session, select, delete
from config import app
from Models.IndependentModels import *
from HelperFunctions import *
# ===========================test functions===========================


@app.delete("/courseSkillRelations/deleteall")
def deleteAll():
    return deleteAllData(CourseSkillRelationModel)


# ===========================actual CRUD functions===========================
# input should be an array
# requests contains "CourseId" and a list "skills" which contains the Skill_ID of the skills to add
@app.post('/courseSkillRelations/')
async def addcourseSkillRelation(request: Request, session: Session = Depends(get_session)):
    errors = []
    try:
        requestData = await request.json()
        course = session.get(CourseModel, requestData["Course_ID"])
        if course == None:
            errors.append("Course does not exist!")
            return {
                "success": False,
                "message": errors
            }
        for Skill_ID in requestData["skills"]:
            newRoleSkillRelation = CourseSkillRelationModel()
            newRoleSkillRelation.Course_ID = requestData["Course_ID"]
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
            "message": "Skill(s) assigned to course"
        }
    except Exception as e:
        errors.append(str(e))
        return {
            "success": False,
            "message": errors
        }
