from fastapi import Response, Depends
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
@app.post('/courseSkillRelations/')
def addcourseSkillRelation(courseSkillRelation: CourseSkillRelationModel, session: Session = Depends(get_session)):
    errors = []
    try:
        print("courseSkillRelation", courseSkillRelation)
        print("courseSkillRelation", courseSkillRelation.Role_ID)
        print("courseSkillRelation", courseSkillRelation.Skill_ID)
        course = session.get(CourseModel, courseSkillRelation.Role_ID)
        skill = session.get(SkillModel, courseSkillRelation.Skill_ID)
        if course == None:
            errors.append("Course does not exist!")
        if skill == None:
            errors.append("Skill does not exist")
        if len(errors) > 0:
            return {
                "success": False,
                "message": errors
            }
        session.add(courseSkillRelation)
        session.commit()
        session.refresh(courseSkillRelation)
        session.close()
        return {
            "success": True,
            "message": "Skill assigned to course"
        }
    except Exception as e:
        errors.append(str(e))
        return {
            "success": False,
            "message": errors
        }
