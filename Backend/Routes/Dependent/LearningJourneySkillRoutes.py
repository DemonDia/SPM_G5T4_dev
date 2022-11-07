from fastapi import Response, Depends
from database import *
from sqlmodel import Session, select, delete, join
from config import app
from Models.DependentModels import LearningJourneySkillRelationModel

from HelperFunctions import *
from fastapi import Request

@app.delete("/learningjourneyskillrelation/deleteall",tags=["LearningJourneySkillRelation","DeleteAll"])
def deleteAll():
    return deleteAllData(LearningJourneySkillRelationModel)