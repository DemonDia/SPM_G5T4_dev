

from fastapi import Response, Depends, Request
from Models.DependentModels import CourseSkillRelationModel
from database import *
from sqlmodel import Session, select, delete, join
from config import app
from Models.IndependentModels import *
from HelperFunctions import *


@app.post("/skillcourserelations/byid", tags=["CourseSkillRelation"])
async def getCoursesbySkills(request: Request, session: Session = Depends(get_session)):
    errors = []
    try:
        requestData = await request.json()
        isInterrupted = False
        # get all skills
        allSkillStatement = select(SkillModel)
        allSkills = session.exec(allSkillStatement).all()
        skillDict = {}
        for skill in allSkills:
            Curr_Skill_ID = skill.Skill_ID
            Curr_Skill_Name = skill.Skill_Name
            skillDict[Curr_Skill_ID] = Curr_Skill_Name
            
        for Skill_ID in requestData["Skills"]:
            # compare, if not found, just break
            if Skill_ID not in skillDict.keys():
                isInterrupted = True
                break
        if isInterrupted:
            errors.append("Skill(s) are not found")
            # get all courses

        allCoursesStataement = select(CourseModel)
        allCourses = session.exec(allCoursesStataement).all()
        courseDict = {}
        for course in allCourses:
            Curr_Course_ID = course.Course_ID
            Curr_Course_Name = course.Course_Name
            courseDict[Curr_Course_ID] = Curr_Course_Name
        # get all the relations
        print(skillDict.keys())

        allCourseSkillRelationStatement = select(CourseSkillRelationModel)
        allCourseSkillRelations = session.exec(
            allCourseSkillRelationStatement).all()

        # loop through selected relations
        # courses and skills to be returned
        selectedRelations = []
        for relation in allCourseSkillRelations:
            print("relation.Skill_ID",relation.Skill_ID)
            if relation.Skill_ID in requestData["Skills"]:
                newRelationRow = {}
                newRelationRow["Skill_ID"] = relation.Skill_ID
                newRelationRow["Skill_Name"] = skillDict[relation.Skill_ID]
                newRelationRow["Course_ID"] = relation.Course_ID
                newRelationRow["Course_Name"] = courseDict[relation.Course_ID]
                selectedRelations.append(newRelationRow)

        if len(errors) > 0:
            return {
                "success": False,
                "message": errors
            }
        return {
            "success": True,
            "data": selectedRelations
        }
    except Exception as e:
        errors.append(str(e))
        return {
            "success": False,
            "message": errors
        }
