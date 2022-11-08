

# ===============test client===============
from fastapi.testclient import TestClient
import pytest
from main import app
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

# ========================================FastAPI test========================================


@pytest.fixture(autouse=True)
def tests():
    cleanUp()
    seedAllData()
    yield
    cleanUp()


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200


# ======================================== Role Tests ========================================
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

    createRoleWithLongName = client.post("/roles/",
                                      json={
                                          "Role_Name": "This is a role with long name!a",
                                          "Role_Description": "Product Manager needs to collaborate effectively with cross-functional stakeholders to create a smooth user experience for job seekers and employers",
                                          "Active": True
                                      })
    assert createRoleWithLongName.json()["success"] == False

    createRoleWithLongDesc = client.post("/roles/",
                                      json={
                                          "Role_Name": "Product Manager Head",
                                          "Role_Description": "Lorem ipsum dolor sit amet, consectetuer adipiscing elit.Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes,nasaaa",
                                          "Active": True
                                      })
    assert createRoleWithLongDesc.json()["success"] == False


def test_view_available_roles():
    beforeAllRoles = len(client.get("/roles/").json()["data"])
    beforeAvailableRoles = len(client.get("/roles/available/").json()["data"])
    client.post("/roles/",
                json={
                    "Role_Name": "Unavailable role",
                    "Role_Description": "....",
                    "Active": False
                })
    afterAllRoles = len(client.get("/roles/").json()["data"])
    afterAvailableRoles = len(client.get("/roles/available/").json()["data"])
    assert afterAllRoles > beforeAllRoles
    assert beforeAvailableRoles == afterAvailableRoles


def test_role_update():
    beforeUpdate = client.get("/roles/{id}/".format(id=1))
    beforeUpdateData = beforeUpdate.json()["data"]
    updateRole = client.put("/roles/{id}/".format(id=1), json={
        "Role_Name": "Cleaner",
        "Role_Description": "Clean common areas, toilets",
        "Active": True
    })
    afterUpdate = client.get("/roles/{id}/".format(id=1))
    afterUpdateData = afterUpdate.json()["data"]
    assert updateRole.json()["success"] == True and beforeUpdateData["Role_Name"] != afterUpdateData["Role_Name"] and beforeUpdateData["Role_Description"] != afterUpdateData["Role_Description"]


def test_delete_role():
    deleteRole = client.put("/roles/delete/{id}/".format(id=1))
    assert deleteRole.json()["success"] == True
    getCurrentRole = client.get("/roles/{id}/".format(id=1))
    assert getCurrentRole.json()["data"]["Active"] == False


# ======================================== Skill Tests ========================================
def test_get_skills():
    response = client.get("/skills/")
    assert response.json()["success"] == True

def test_add_skill():
    createNewSkill = client.post("/skills/", json={
        "Skill_Name": "Leadership",
        "Skill_Description": "“Strengths and abilities individuals demonstrate that help to oversee processes, guide initiatives and steer their employees toward the achievement of goals.",
        "Active": True
    })
    assert createNewSkill.json()["success"] == True

    createDuplicateSkill = client.post("/skills/", json={
        "Skill_Name": "Leadership",
        "Skill_Description": "Analytical skills in data science to visualise data",
        "Active": True
    })
    assert createDuplicateSkill.json()["success"] == False

    createSkillWithLongName = client.post("/skills/", json={
        "Skill_Name": "Teamworkkkkkkkkkkkkkkkkkkkkkkkk",
        "Skill_Description": "Working with people from different places",
        "Active": True
    })
    assert createSkillWithLongName.json()["success"] == False

    createSkillWithLongDesc = client.post("/skills/",json={
        "Skill_Name":"Long name",
        "Skill_Description":"...........................................................................................................................................................................",
        "Active":True
    })
    assert createSkillWithLongDesc.json()["success"] == False

def test_view_available_skills():
    beforeAllSkills = len(client.get("/skills/").json()["data"])
    beforeAvailableSkills = len(client.get("/skills/available/").json()["data"])
    client.post("/skills/",
                json={
                    "Skill_Name": "Unavailable skill",
                    "Skill_Description": "....",
                    "Active": False
                })
    afterAllSkills = len(client.get("/skills/").json()["data"])
    afterAvailableSkills = len(client.get("/skills/available/").json()["data"])
    assert afterAllSkills > beforeAllSkills
    assert beforeAvailableSkills == afterAvailableSkills

def test_skill_update():
    beforeUpdate = client.get("/skills/{id}/".format(id=1))
    beforeUpdateData = beforeUpdate.json()["data"]
    updateRole = client.put("/skills/{id}/".format(id=1), json={
        "Skill_Name": "Eating",
        "Skill_Description": "eating is good.",
        "Active": True
    })
    afterUpdate = client.get("/skills/{id}/".format(id=1))
    afterUpdateData = afterUpdate.json()["data"]
    assert updateRole.json()["success"] == True and beforeUpdateData["Skill_Name"] != afterUpdateData["Skill_Name"] \
        and beforeUpdateData["Skill_Description"] != afterUpdateData["Skill_Description"]

def test_delete_skill():
    deleteSkill = client.put("/skills/delete/{id}/".format(id=1))
    assert deleteSkill.json()["success"] == True
    getCurrentSkill = client.get("/skills/{id}/".format(id=1))
    assert getCurrentSkill.json()["data"]["Active"] == False