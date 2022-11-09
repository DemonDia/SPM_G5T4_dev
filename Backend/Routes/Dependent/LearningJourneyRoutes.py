from fastapi import Response, Depends
from database import *
from sqlmodel import Session, select, delete, join
from config import app
from Models.DependentModels import LearningJourneyModel, CourseLearningJourneyModel
from Models.IndependentModels import CourseModel, StaffModel

from HelperFunctions import *
from fastapi import Request

# ===========================test functions===========================


@app.post("/learningjourney/seedall",tags=["LearningJourney","SeedAll"])
def seedAll():
    return seedInitialData("learningjourney", LearningJourneyModel, 25, True)


@app.delete("/learningjourney/deleteall",tags=["LearningJourney","DeleteAll"])
def deleteAll():
    return deleteAllData(LearningJourneyModel)

# ===========================helper functions===========================


def getRelatedCourses(targetModelIdValue):
    try:
        session = Session(engine)
        statement = select(CourseModel.Course_ID, CourseModel.Course_Name).select_from(join(CourseModel, CourseLearningJourneyModel)).where(
            CourseLearningJourneyModel.LearningJourney_ID == targetModelIdValue)
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
def getRelatedSkills(targetModelIdValue):
    try:
        session = Session(engine)
        statement = select(SkillModel.Skill_ID, SkillModel.Skill_Name).select_from(join(SkillModel, LearningJourneySkillRelationModel)).where(
            LearningJourneySkillRelationModel.LearningJourney_ID == targetModelIdValue)
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


def getAllRelatedCourses():
    try:
        courseDict = {}
        session = Session(engine)
        statement = select(CourseModel.Course_Name, LearningJourneyModel.LearningJourney_ID).select_from(
            join(LearningJourneyModel, join(CourseModel, CourseLearningJourneyModel)))
        results = session.exec(statement).all()
        for result in results:
            if (result.LearningJourney_ID not in courseDict.keys()):
                courseDict[result.LearningJourney_ID] = [result.Course_Name]
            else:
                courseDict[result.LearningJourney_ID].append(
                    result.Course_Name)
        print(courseDict)
        return {
            "success": True,
            "data": courseDict
        }
    except Exception as e:
        return {
            "success": False,
            "message": e,
            "data": []
        }

# ===========================actual CRUD functions===========================


@app.post("/learningjourney/",tags=["LearningJourney"])
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

        newLearningJourney = LearningJourneyModel(
            Staff_ID=staffId, Role_ID=roleId)
        session.add(newLearningJourney)
        courses = requestData["Courses"]
        for Course_ID in courses:
            selectedCourseStatement = select(CourseModel).where(
                CourseModel.Course_ID == Course_ID)
            selectedCourseStatementResult = session.exec(
                selectedCourseStatement)
            selectedCourseStatementResult = selectedCourseStatementResult.all()
            if (len(selectedCourseStatementResult) == 0):
                errors.append("Course does not exist")
                break
            newCourseLearningJourneyRelation = CourseLearningJourneyModel()
            newCourseLearningJourneyRelation.Course_ID = Course_ID
            newCourseLearningJourneyRelation.LearningJourney_ID = newLearningJourney.LearningJourney_ID
            session.add(newCourseLearningJourneyRelation)
        
        skills = requestData["Skills"]
        for Skill_ID in skills:
            selectedSkillStatement = select(SkillModel).where(
                SkillModel.Skill_ID == Skill_ID)
            selectedSkillStatementResult = session.exec(
                selectedSkillStatement)
            selectedSkillStatementResult = selectedSkillStatementResult.all()
            if (len(selectedSkillStatementResult) == 0):
                errors.append("Skill does not exist")
                break
            newSkillLearningJourneyRelation = LearningJourneySkillRelationModel()
            newSkillLearningJourneyRelation.Skill_ID = Skill_ID
            newSkillLearningJourneyRelation.LearningJourney_ID = newLearningJourney.LearningJourney_ID
            session.add(newSkillLearningJourneyRelation)

        if (len(errors) > 0):
            return {
                "success": False,
                "message": errors
            }

        session.commit()
        session.refresh(newLearningJourney)
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


@app.get('/learningjourney/',tags=["LearningJourney"])
def getLearningJourney(session: Session = Depends(get_session)):
    errors = []
    try:
        stmt = select(LearningJourneyModel)
        getAllLearningJourneys = session.exec(stmt).all()
        allCourses = getAllRelatedCourses()["data"]
        allLearningJourneys = []
        for learningJourney in getAllLearningJourneys:
            learningJourneyDict = {}
            for columnName, columnValue in learningJourney:
                learningJourneyDict[columnName] = columnValue
                if learningJourney.LearningJourney_ID in allCourses.keys():
                    learningJourneyDict["Courses"] = allCourses[learningJourney.LearningJourney_ID]
                else:
                    learningJourneyDict["Courses"] = []

            allLearningJourneys.append(learningJourneyDict)
        return {
            "success": True,
            "data": allLearningJourneys,
        }
    except Exception as e:
        print(e)
        errors.append(str(e))
        return {
            "success": False,
            "message": errors
        }


@app.get("/learningjourney/{LearningJourney_ID}/",tags=["LearningJourney"])
def getLearningJourneyById(LearningJourney_ID: int, session: Session = Depends(get_session)):
    errors = []
    try:
        learningJourney = session.get(LearningJourneyModel, LearningJourney_ID)
        # role not found
        if not learningJourney:
            errors.append("Learning journey not found")

        if len(errors) > 0:
            return {
                "success": False,
                "message": errors
            }
        learningJourneyDict = {}
        for columnName, columnValue in learningJourney:
            learningJourneyDict[columnName] = columnValue
        relatedCourses = getRelatedCourses(learningJourney.LearningJourney_ID)
        relatedSkills = getRelatedSkills(learningJourney.LearningJourney_ID)
        learningJourneyDict["Courses"] = relatedCourses["data"]
        learningJourneyDict["Skills"] = relatedSkills["data"]
        # return role
        return {
            "success": True,
            "data": learningJourneyDict
        }
    except Exception as e:
        errors.append(str(e))
        return {
            "success": False,
            "message": errors
        }


@app.get("/learningjourney/staff/{Staff_ID}",tags=["LearningJourney"])
def getLearningJourneyByStaff(Staff_ID: int, session: Session = Depends(get_session)):
    errors = []
    try:
        # find staff
        checkSelectedStaffStatement = select(
            StaffModel).where(StaffModel.Staff_ID == Staff_ID)
        selectedStaff = session.exec(checkSelectedStaffStatement).all()
        print("selectedStaff", selectedStaff)
        if len(selectedStaff) == 0:
            errors.append("Staff not found")

        getLearningJourneyByStaffStatement = select(LearningJourneyModel).where(
            LearningJourneyModel.Staff_ID == Staff_ID)
        learningJourneys = session.exec(
            getLearningJourneyByStaffStatement).all()
        staffLearningJourneyList = []
        allCoursesToLearningJourney = getAllRelatedCourses()["data"]
        for learningJourney in learningJourneys:
            learningJourneyDict = {}
            for columnName, columnValue in learningJourney:
                if columnName != "Role_ID":
                    learningJourneyDict[columnName] = columnValue
            # set role
            selectedRoleStatement = select(RoleModel).where(RoleModel.Role_ID == learningJourney.Role_ID)  
            selectedRole = session.exec(selectedRoleStatement).all()
            if(len(selectedRole) == 0):
                learningJourneyDict["Role"] = {}
            else:
                learningJourneyDict["Role"] = selectedRole[0]
            if learningJourneyDict["LearningJourney_ID"] not in allCoursesToLearningJourney.keys():
                learningJourneyDict["Courses"] = []
            else:
                learningJourneyDict["Courses"] = allCoursesToLearningJourney[learningJourneyDict["LearningJourney_ID"]]
            staffLearningJourneyList.append(learningJourneyDict)

        if len(errors) > 0:
            return {
                "success": False,
                "message": errors
            }

        # get all the LJs
        return {
            "success": True,
            "data": staffLearningJourneyList
        }
    except Exception as e:
        errors.append(str(e))
        return {
            "success": False,
            "message": errors
        }


@app.delete("/learningjourney/{LearningJourney_ID}/",tags=["LearningJourney"])
def deleteLearningJourney(LearningJourney_ID: int, session: Session = Depends(get_session)):
    errors = []
    try:
        # find the learning journey
        selectedLearningJourneyStatement = select(LearningJourneyModel).where(LearningJourneyModel.LearningJourney_ID == LearningJourney_ID)
        selectedLearningJourney = session.exec(selectedLearningJourneyStatement).all()
        if(len(selectedLearningJourney) == 0):
            errors.append("Learning journey does not exist!")
        else:
            selectedLearningJourney = selectedLearningJourney[0]
        

        # delete all the relations
        # hard delete the relations
        allCourseRelatedRelationStatement = select(CourseLearningJourneyModel).where(
            CourseLearningJourneyModel.LearningJourney_ID == LearningJourney_ID)
        courseRelationResults = session.exec(allCourseRelatedRelationStatement)
        allCourseRelations = courseRelationResults.all()
        for relation in allCourseRelations:
            session.delete(relation)
        

        allSkillRelatedRelationStatement = select(LearningJourneySkillRelationModel).where(
            LearningJourneySkillRelationModel.LearningJourney_ID == LearningJourney_ID)
        skillRelationResults = session.exec(allSkillRelatedRelationStatement)
        allSkillRelations = skillRelationResults.all()
        for skill in allSkillRelations:
            session.delete(skill)
    
        session.delete(selectedLearningJourney)
        session.commit()
        session.close()
        return {
            "success": True,
            "message": "Learning journey deleted"
        }
    except Exception as e:
        errors.append(str(e))
        return {
            "success": False,
            "message": errors
        }
