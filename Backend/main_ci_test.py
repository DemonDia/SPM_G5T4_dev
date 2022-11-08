

# ===============test client===============
from fastapi.testclient import TestClient
import pytest
from main import app
# ============================adding tests============================
# def mainTest():
#     # trigger test cases for each entity
#     testAllRoleCases()
#     testAllSkillCases()
#     testAllRoleSkillRelationCases()
#     testAllCourseSkillRelationCases()
#     testAllLearningJourneyCases()
#     testAllCourseLearningJourneyCases()
#     testAllLearningJourneySkillRelationCases()
#     # remove all the test data after testing is complete


# ============================Helper functions/variables============================
entities = ["roles", "skills", "course", "userroles", "roleskillrelations", "courseskillrelations",
            "staff", "learningjourney", "courselearningjourney", "learningjourneyskillrelation"]
client = TestClient(app)
# setup data


def seedAllData():
    for entity in entities:
        client.post(entity+"/seedall")

# delete ALL the testing data


def cleanUp():
    for entity in range(len(entities)-1, -1, -1):
        client.delete(entities[entity]+"/deleteall")

# ============================FastAPI test============================


@pytest.fixture(autouse=True)
def tests():
    cleanUp()
    seedAllData()
    yield
    cleanUp()


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200


# ========================== Role Tests ==========================
def test_get_roles():
    response = client.get("/roles/")
    assert response.json()["success"] == True


def test_post_roles():
    createNewRole = client.post("/roles/",
                             json={
                                 "Role_Name": "Product Manager",
                                 "Role_Description": "Product Manager needs to collaborate effectively with cross-functional stakeholders to create a smooth user experience for job seekers and employers",
                                 "Active": True
                             })
    
    assert createNewRole.json()["success"] == True
    createDuplicateRole = client.post("/roles/",
                             json={
                                 "Role_Name": "Product Manager",
                                 "Role_Description": "Product Manager needs to collaborate effectively with cross-functional stakeholders to create a smooth user experience for job seekers and employers",
                                 "Active": True
                             })
    assert createDuplicateRole.json()["success"] == False
