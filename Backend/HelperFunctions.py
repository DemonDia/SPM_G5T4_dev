import pathlib
from sqlmodel import Session, select, delete
from database import *
from ColumnNames import dataColumns
from datetime import datetime

#each field for each column, returns column value
def createColumnValue(columnName,columnType, currentIndex):
    if columnType == "str":
        return "{columnName} #{value}".format(columnName = columnName, value = str(currentIndex))
    if columnType == "float":
        return float(currentIndex)
    if columnType == "int":
        return int(currentIndex)
    if columnType == "boolean":
        return True
    if columnType == "datetime":
        return datetime.now()
    return None

#create records with given size (yet to be inserted into the database)
def createRecords(modelName,noOfRecords):
    # to return
    records = []

    columns = dataColumns[modelName]
    for i in range(1,noOfRecords+1):
        currentRecord = {}
        # each column
        for columnName,columnType in columns:
            currentRecord[columnName] = createColumnValue(columnName,columnType,i)
        records.append(currentRecord)
    return records



# seed data for given entity
def seedInitialData(modelName,model,NoOfRecords = 25):
    try:
        session = Session(engine)
        stmt = select(model)
        result = session.exec(stmt).first()
        # check if duplicates
        if result is None:
            # autogen data
            recordsToAdd = createRecords(modelName,NoOfRecords)
            for record in recordsToAdd:
                session.add(model(**record))
            session.commit()
        session.close()

        return {
            "success":True,
            "message":"Data is seeded"
        }
    except Exception as e:
        return {
            "success":False,
            "messaage":e
        }

# delete all data for given entity
def deleteAllData(model):
    session = Session(engine)
    stmt = delete(model)
    result = session.exec(stmt)
    session.commit()
    session.close()
    if result:
        return {
            "success":True,
            "message":"Everything is deleted"
        }
    return {
        "success":False,
        "message":"Failed to delete"
    }
