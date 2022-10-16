from fastapi import Response, Depends
from database import *
from sqlmodel import Session, select, delete, join
from config import app
from Models.IndependentModels import CourseModel
from HelperFunctions import *
# ===========================test functions===========================


@app.delete("/course/deleteall")
def deleteAll():
    return deleteAllData(CourseModel)


@app.post("/course/seedall")
def addSeedData():
    return seedInitialData("course", CourseModel, 25, False, "courses")

# ===========================helper functions===========================


def getRelatedSkills(targetModelIdValue):
    try:
        session = Session(engine)
        statement = select(SkillModel.Skill_Name).select_from(join(SkillModel, CourseSkillRelationModel)).where(
            CourseSkillRelationModel.Skill_ID == SkillModel.Skill_ID)
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
        statement = select(SkillModel.Skill_Name, CourseModel.Course_ID).select_from(
            join(CourseModel, join(SkillModel, CourseSkillRelationModel)))
        results = session.exec(statement).all()
        for result in results:
            if (result.Course_ID not in skillDict.keys()):
                skillDict[result.Course_ID] = [result.Skill_Name]
            else:
                skillDict[result.Course_ID].append(result.Skill_Name)
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


@app.get('/course/')
def getCourse(session: Session = Depends(get_session)):
    errors = []
    try:
        stmt = select(CourseModel)
        getAllCourses = session.exec(stmt).all()
        allSkills = getAllRelatedSkills()["data"]
        print(allSkills)
        allCourses = []
        for course in getAllCourses:
            roleDict = {}
            for columnName, columnValue in course:
                roleDict[columnName] = columnValue
                if course.Course_ID in allSkills.keys():

                    roleDict["Skills"] = allSkills[course.Course_ID]
                else:
                    roleDict["Skills"] = []
            allCourses.append(roleDict)
        return {
            "success": True,
            "data": allCourses,
        }
    except Exception as e:
        print(e)
        errors.append(str(e))
        return {
            "success": False,
            "message": errors
        }


@app.get('/course/available/')
def getCourse(session: Session = Depends(get_session)):
    errors = []
    try:
        stmt = select(CourseModel).where(CourseModel.Course_Status == "Active")
        availableCourses = session.exec(stmt).all()
        allSkills = getAllRelatedSkills()["data"]
        allCourses = []
        for course in availableCourses:
            roleDict = {}
            for columnName, columnValue in course:
                roleDict[columnName] = columnValue
                if course.Course_ID in allSkills.keys():

                    roleDict["Skills"] = allSkills[course.Course_ID]
                else:
                    roleDict["Skills"] = []
            allCourses.append(roleDict)
        return {
            "success": True,
            "data": allCourses,
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
        course = session.get(CourseModel, course_ID)
        # role not found
        if not course:
            errors.append("Course not found")

        if len(errors) > 0:
            return {
                "success": False,
                "message": errors
            }
        courseDict = {}
        for columnName, columnValue in course:
            courseDict[columnName] = columnValue
        outcome = getRelatedSkills(course.Course_ID)
        courseDict["Skills"] = outcome["data"]
        # return course
        return {
            "success": True,
            "data": courseDict
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
