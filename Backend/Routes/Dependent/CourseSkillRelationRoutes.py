from fastapi import Response, Depends, Request
from Models.DependentModels import CourseSkillRelationModel
from database import *
from sqlmodel import Session, select, delete,join
from config import app
from Models.IndependentModels import *
from HelperFunctions import *
# ===========================test functions===========================


@app.delete("/courseskillrelations/deleteall")
def deleteAll():
    return deleteAllData(CourseSkillRelationModel)


# ===========================actual CRUD functions===========================
# input should be an array
# requests contains "CourseId" and a list "skills" which contains the Skill_ID of the skills to add
@app.post('/courseskillrelations/')
async def addSkillsToCourses(request: Request, session: Session = Depends(get_session)):
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
        for Skill_ID in requestData["Skills"]:
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

@app.get('/courseskillrelations/{Course_ID}')
async def addRoleSkillRelation(Course_ID: str, session: Session = Depends(get_session)):
    errors = []
    try:
        role = session.get(CourseModel, Course_ID)
        if role == None:
            errors.append("Role does not exist!")
            errors.append(str(e))
            return {
                "success": False,
                "message": errors
            }
        statement = select(SkillModel.Skill_Name, SkillModel.Skill_ID).select_from(
            join(CourseModel, join(SkillModel, CourseSkillRelationModel))).where(CourseModel.Course_ID == Course_ID)
        results = session.exec(statement).all()

        if len(errors) > 0:
            return {
                "success": False,
                "message": errors
            }

        return {
            "success": True,
            "data": results
        }

    except Exception as e:
        errors.append(str(e))
        return {
            "success": False,
            "message": errors
        }


@app.put('/courseskillrelations/{Course_ID}')
async def updateCourseSkillRelations(Course_ID: str, request: Request, session: Session = Depends(get_session)):
    errors = []
    try:
        requestData = await request.json()
        statement = select(CourseModel).where(
            CourseModel.Course_ID == Course_ID)
        result = session.exec(statement)

        chosenRoleResult = result.all()
        if len(chosenRoleResult) == 0:
            return  # yes this returns the success = false json
        else:
            role = chosenRoleResult[0]
        if role == None:
            errors.append("Role does not exist!")
            errors.append(str(e))
            return {
                "success": False,
                "message": errors
            }

        # delete relations
        existingCourseSkillStatement = select(
            CourseSkillRelationModel).where(CourseSkillRelationModel.Course_ID == Course_ID)
        allExistingCourseSkillRelations = session.exec(
            existingCourseSkillStatement)
        allRelations = allExistingCourseSkillRelations.all()
        for relation in allRelations:
            session.delete(relation)

        # add again
        for Skill_ID in requestData["Skills"]:
            newRoleSkillRelation = CourseSkillRelationModel()
            newRoleSkillRelation.Course_ID = Course_ID
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
            "message": "Related skills are updated!"
        }

    except Exception as e:
        errors.append(str(e))
        return {
            "success": False,
            "message": errors
        }
