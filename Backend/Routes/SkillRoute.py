from fastapi import Response, Depends
from Schema.TrackSchema import Track
from database import *
from sqlmodel import Session, select, delete
from config import  app
from Models.SkillModel import Skill
from HelperFunctions import *


@app.get('/tracks/')
def getTracks(session: Session = Depends(get_session)):
    stmt = select(SkillModel)
    result = session.exec(stmt).all()
    # return result
    return {
        "success": True,
        "data": result
    }
