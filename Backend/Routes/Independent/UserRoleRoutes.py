from fastapi import Response, Depends
from Schema.IndependentSchema import Skill
from database import *
from sqlmodel import Session, select, delete, join
from config import app
from Models.IndependentModels import UserRoleModel
from HelperFunctions import *

# ===========================test functions===========================

@app.delete("/userroles/deleteall")
def deleteAll():
    return deleteAllData(UserRoleModel)


@app.post("/userroles/seedall")
def addSeedData():
    return seedInitialData("userroles", UserRoleModel, 25, False, "role")

