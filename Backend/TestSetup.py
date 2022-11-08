import requests
from fastapi.testclient import TestClient
from main import app
entities = ["roles","skills","course","userroles","roleskillrelations","courseskillrelations","staff","learningjourney","courselearningjourney","learningjourneyskillrelation"]
client = TestClient(app)
# delete all data
def deleteAll(url):
    results = requests.delete(url+"deleteall")
    return results.json()

# seed data for individual entity
def seedData(url):
    results = requests.post(url+"seedall")
    return results.json()

def seedAllData():
    for entity in entities:
        
        req = client.post("/"+entity+"/seedall")
        # if entity == "staff":
        #     assert req.json() == None

# delete ALL the testing data


def cleanUp():
    for entity in range(len(entities)-1, -1, -1):
        client.delete("/"+entities[entity]+"/deleteall")

def mainSetup():
    print("=========================Setup begin=========================")
    cleanUp()
    seedAllData()
    print("=========================Setup done=========================")

if __name__ == "__main__":
    mainSetup()
