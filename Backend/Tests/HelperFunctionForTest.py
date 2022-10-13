import requests
# =====================Universal variables=====================
# name of entities 
entities = ["roles","skills"] 

# name of operations (based on CRUD)
# Names:
# create --> create new entity
# readAll --> read all existing rows
# readById --> read by specific Id
operationTypes = ["create","readAll","readById","updateById","softDelete"]

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
    try:
        if entityName not in entities:
             print(entityName+" not found. Unable to test")
             print("Interrupted")
        print("============================================")
        print(testCaseName)
        print("Input:",inputJson)
        if operationType == "create":
            triggeredTestCase = addRow(BASE+entityName, inputJson)
        if operationType == "readAll":
            triggeredTestCase = getAllRows(BASE+entityName)
        if operationType == "readById":
            triggeredTestCase = getSingleRow(BASE+entityName, fieldValue)
        if operationType == "updateById":
            triggeredTestCase = updateRow(BASE+entityName,fieldValue,inputJson)
        if operationType == "softDelete":
            triggeredTestCase = softDeleteRow(BASE+entityName,fieldValue)
        print(triggeredTestCase)
        # print(getErrorMessage(triggeredTestCase))
        validateOutcome(triggeredTestCase, expectedResult)
        print("Complete")
    except Exception as e:
        print("Issue: ",str(e))
        print("Interrupted")

# to get error msg
def getErrorMessage(testCaseResult):
    if testCaseResult["success"] == True:
        return "N/A"
    return testCaseResult["message"]

# setup data
def seedAllData():
    for entity in entities:
        seedData(BASE+entity+"/")

# delete ALL the testing data
def cleanUp():
    for entity in entities:
        deleteAll(BASE+entity+"/")

# check if test case pass
def validateOutcome(actualResult, expectedResult):
    try:
        if actualResult["success"] == expectedResult:
            print("Test case passed")
        else:
            print("Test case failed")
    except:
        print("Test case failed")
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

# Gets all rows
def getAllRows(url):
    rows = requests.get(url)
    return rows.json()

# Add row
def addRow(url,jsonObject):
    addedRow = requests.post(url, json=jsonObject)
    return addedRow.json()
# Update rows
def updateRow(url, rowId,jsonObject):
    updatedRow = requests.put(url+"/{rowId}".format(rowId=rowId),json = jsonObject)
    return updatedRow.json()

def softDeleteRow(url,rowId):
    softDeleted = requests.put(url+"/delete/{rowId}".format(rowId=rowId))
    return softDeleted.json()

# Delete rows
def deleteRow(url, rowId):
    deletedRow = requests.delete(url+"{rowId}".format(rowId=rowId))
    return deletedRow.json()