from fastapi import Response, Depends
from database import *
from sqlmodel import Session, select, delete, join
from config import app
from Models.IndependentModels import UserRoleModel
from HelperFunctions import *

# ===========================test functions===========================

@app.delete("/userroles/deleteall",tags=["UserRoles","DeleteAll"])
def deleteAll():
    return deleteAllData(UserRoleModel)


@app.post("/userroles/seedall",tags=["UserRoles","SeedAll"])
def addSeedData():
    return seedInitialData("userroles", UserRoleModel, 25, False, "role")

