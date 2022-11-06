import requests
# =====================Universal variables=====================
# name of entities
entities = ["roles","skills","course","userroles","roleskillrelations","courseskillrelations","staff","learningjourney","courselearningjourney","courselearningjourney"]

# name of operations (based on CRUD)
# Names:
# create --> create new entity
# readAll --> read all existing rows
# readById --> read by specific Id
operationTypes = ["create","readAll","readAllAvailable","readById","updateById","softDelete","hardDelete","addRelation","readByStaffId","readByStaffIDorEmail","getAllByIds","deleteRelation"]

# base URL
BASE = "http://127.0.0.1:8000/"
# =====================Other helper functions=====================
# for testing ONLY
# Trigger test case
# testCaseName (str) --> name of test case
# expectedResult (bool) --> expected value of 'success'
# entityName (str) --> name of entity; from 'entities' list
# inputJson (dict) --> the input of the test case
# operationType (str) --> CRUD; from 'operationTypes' list
# fieldValue (any) --> value of given field; default is None
def triggerTestCase(testCaseName,expectedResult,entityName,inputJson = None,operationType = "readAll",fieldValue = None):
    # assert entityName in entities,"Entity name '"+ entityName+"' not found. Unable to test"
    assert operationType in operationTypes, "Operation type '"+operationType+"' not found. Unable to test"
    print("============================================")
    print(testCaseName)
    print("Input:",inputJson)
    if operationType == "create":
        triggeredTestCase = addRow(BASE+entityName+"/", inputJson)
    if operationType == "readAll":
        triggeredTestCase = getAllRows(BASE+entityName)
    if operationType == "readAllAvailable":
        triggeredTestCase = getAllRows(BASE+entityName+"/available")
    if operationType == "readById":
        triggeredTestCase = getSingleRow(BASE+entityName, fieldValue)
    if operationType == "readByStaffId":
        triggeredTestCase = getByStaffId(BASE+entityName,fieldValue)
    if operationType == "updateById":
        triggeredTestCase = updateRow(BASE+entityName,fieldValue,inputJson)
    if operationType == "softDelete":
        triggeredTestCase = softDeleteRow(BASE+entityName,fieldValue)
    if operationType == "addRelation":
        triggeredTestCase = addRelation(BASE+entityName,inputJson)
    if operationType == "hardDelete":
        triggeredTestCase = deleteRow(BASE+entityName,fieldValue)
    if operationType == "deleteRelation":
        triggeredTestCase = deleteRelation(BASE+entityName,inputJson)
    if operationType == "readByStaffIDorEmail":
        triggeredTestCase = getByStaffEmailOrID(BASE+entityName,inputJson)
    if operationType == "getAllByIds":
        triggeredTestCase = getByIDs(BASE+entityName,inputJson)
    validateOutcome(triggeredTestCase, expectedResult,testCaseName)
    print("Complete")


# setup data
def seedAllData():
    for entity in entities:
        seedData(BASE+entity+"/")

# delete ALL the testing data
def cleanUp():
    for entity in range(len(entities)-1,-1,-1):
        print("entities[entity]",entities[entity])
        deleteAll(BASE+entities[entity]+"/")

# check if test case pass
def validateOutcome(actualResult, expectedResult,testCaseName):
    if(actualResult["success"] != expectedResult):
        print(actualResult["message"])
    assert actualResult["success"] == expectedResult, "Test case '"+testCaseName+"' failed"

# delete all data
def deleteAll(url):
    results = requests.delete(url+"deleteall")
    return results.json()

# seed data for individual entity
def seedData(url):
    results = requests.post(url+"seedall")
    return results.json()

# reset to defaults
# MAY NOT BE USED; just ignore
def resetDataToDefaults(url):
    deleteResults = deleteAll(url)
    seedResults = seedData(url)

    returningResult = deleteResults["success"] == seedResults["success"]
    message = ""
    if(returningResult):
        message = "Reset successfully"
    else:
        message = "Reset failed"
    return {
        "success" : returningResult,
        "message" : message
    }


# =====================CRUD functions=====================
# Gets single row based on its ID
def getSingleRow(url,rowId):
    obtainedRow = requests.get(url+"/{rowId}".format(rowId=rowId))
    return obtainedRow.json()

def getByStaffId(url,staffId):
    obtainedRow = requests.get(url+"/staff/{staffId}".format(staffId=staffId))
    return obtainedRow.json()

def getByStaffEmailOrID(url,jsonObject):
    obtainedRow = requests.get(url+"/one", json=jsonObject)
    return obtainedRow.json()

def getByIDs(url,jsonObject):
    obtainedRows = requests.get(url+"/byid", json=jsonObject)
    return obtainedRows.json()

# Gets all rows
def getAllRows(url):
    rows = requests.get(url)
    return rows.json()

# Add row
def addRow(url,jsonObject):
    addedRow = requests.post(url, json=jsonObject)
    return addedRow.json()

# Add many to many relation
def addRelation(url,jsonObject):
    addedRelation = requests.post(url+"/", json=jsonObject)
    return addedRelation.json()

def deleteRelation(url,jsonObject):
    deletedRelation = requests.delete(url+"/", json=jsonObject)
    return deletedRelation.json()
# Update rows
def updateRow(url, rowId,jsonObject):
    print(url+"/"+str(rowId))
    updatedRow = requests.put(url+"/{rowId}/".format(rowId=rowId),json = jsonObject)
    return updatedRow.json()

def softDeleteRow(url,rowId):
    softDeleted = requests.put(url+"/delete/{rowId}/".format(rowId=rowId))
    return softDeleted.json()

# Delete rows
def deleteRow(url, rowId):
    deletedRow = requests.delete(url+"/{rowId}/".format(rowId=rowId))
    return deletedRow.json()
