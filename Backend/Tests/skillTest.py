from HelperFunctionsTest import *
BASE = "http://127.0.0.1:8000/skills/"

# ======================Test cases======================
# 1) Delete all data
def deleteAllDataTest():
    print("1) Delete all data")
    result = deleteAll(BASE)
    validateOutcome(result,True)
    print()

# 2) Seed data
def seedDataTest():
    print("2) Seed data")
    result = seedData(BASE)
    validateOutcome(result,True)
    print()

# 3) Reset data to defaults
def resetDataToDefaultTest():
    print("3) Reset data to defaults")
    result = resetDataToDefaults(BASE)
    validateOutcome(result,True)
    print()



# 6) Add data
def addDataTest():
    print("6) Add data")
    print("6)a) Successful adding")
    jsonToAddPass = {
        "Skill_Name":"“Leadership",
        "Skill_Description":"Strengths and abilities individuals demonstrate that help to oversee processes, guide initiatives and steer their employees toward the achievement of goals.",
        "Active": True
    }#change according to schema less ID
    addDataPassResult = addRow(BASE,jsonToAddPass)
    validateOutcome(addDataPassResult,True)

    print("6)b)Unsuccessful adding due to missing fields")
    jsonToAddFail = {
        "Skill_Name":"SE",
        "Active": True
    }#change according to schema less ID
    addDataFailResult = addRow(BASE,jsonToAddFail)
    print("addDataFailResult",addDataFailResult)
    validateOutcome(addDataFailResult,False)
    print()




if __name__ == "__main__":
    deleteAllDataTest()
    seedDataTest()
    resetDataToDefaultTest()
    addDataTest()
