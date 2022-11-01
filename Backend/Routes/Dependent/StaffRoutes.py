from fastapi import Response, Depends
from Schema.IndependentSchema import Skill
from database import *
from sqlmodel import Session, select, delete, join
from config import app
from Models.DependentModels import StaffModel
from HelperFunctions import *

# ===========================test functions===========================

@app.delete("/staff/deleteall",tags=["Staff","DeleteAll"])
def deleteAll():
    return deleteAllData(StaffModel)


@app.post("/staff/seedall",tags=["Staff","SeedAll"])
def addSeedData():
    return seedInitialData("staff", StaffModel, 25, False, "staff")
