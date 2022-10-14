from fastapi import Response, Depends
from database import *
from sqlmodel import Session, select, delete
from config import app
from Models.IndependentModels import CourseModel
from HelperFunctions import *
# ===========================test functions===========================


@app.delete("/course/deleteall")
def deleteAll():
    return deleteAllData(CourseModel)


@app.post("/course/seedall")
def addSeedData():
    return seedInitialData("course", CourseModel)


# ===========================actual CRUD functions===========================
@app.get('/course/')
def getCourse(session: Session = Depends(get_session)):
    errors = []
    try:
        stmt = select(CourseModel)
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


@app.get('/course/available/')
def getCourse(session: Session = Depends(get_session)):
    errors = []
    try:
        stmt = select(CourseModel).where(CourseModel.Active == 1)
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


@app.get("/course/{course_ID}/")
def course(course_ID: str, session: Session = Depends(get_session)):
    errors = []
    try:
        statement = select(CourseModel).where(CourseModel.Course_ID == course_ID)
        result = session.exec(statement)
        course = result.one()
        # course not found
        if not course:
            errors.append("course not found")

        if len(errors) > 0:
            return {
                "success": False,
                "message": errors
            }
        # return course
        return {
            "success": True,
            "data": course
        }
    except Exception as e:
        errors.append(str(e))
        return {
            "success": False,
            "message": errors
        }


@app.post("/course/")
def createCourse(course: CourseModel, session: Session = Depends(get_session)):
    errors = []
    try:
        session.add(course)
        session.commit()
        session.refresh(course)
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
