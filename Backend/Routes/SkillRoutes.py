from fastapi import Response, Depends
from Schema.TrackSchema import Track
from database import *
from sqlmodel import Session, select, delete
from config import  app
from Models.SkillModel import SkillModel
from HelperFunctions import *

@app.delete("/skills/deleteall")
def deleteAll():
    return deleteAllData(SkillModel)

@app.post("/skills/seedall")
def addSeedData():
    return seedInitialData("skill",SkillModel)

# ===========================actual CRUD functions===========================
@app.get('/skills/')
def getSkills(session: Session = Depends(get_session)):
    stmt = select(SkillModel)
    result = session.exec(stmt).all()
    # return result
    return {
        "success": True,
        "data": result
    }

@app.post('/skills/')
def CreateSkills(skill: SkillModel, session: Session = Depends(get_session)):
    try:
        session.add(skill)
        session.commit()
        session.refresh(skill)
        session.close()
        return {
            "success": True,
            "message": "Successfully added"
        }
    except Exception as e:
        return{
            "success": False,
            "message": str(e)
        }
