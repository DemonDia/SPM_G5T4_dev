

# ===============test client===============
from fastapi.testclient import TestClient
import pytest
from main import app
from random import randint

# ============================Helper functions/variables============================
entities = ["roles", "skills", "course", "userroles", "roleskillrelations", "courseskillrelations",
            "staff", "learningjourney", "courselearningjourney", "learningjourneyskillrelation"]
client = TestClient(app)
# setup data


def seedAllData():
    for entity in entities:
        req = client.post("/"+entity+"/seedall")
        # if entity == "staff":
        #     assert req.json() == None

# delete ALL the testing data


def cleanUp():
    for entity in range(len(entities)-1, -1, -1):
        client.delete("/"+entities[entity]+"/deleteall")


# ========================================FastAPI test========================================


@pytest.fixture(autouse=True, scope="session")
def tests():
    cleanUp()
    seedAllData()
    yield
    cleanUp()
    # seedAllData()


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
    assert updateRole.json()["success"] == True and beforeUpdateData["Role_Name"] != afterUpdateData[
        "Role_Name"] and beforeUpdateData["Role_Description"] != afterUpdateData["Role_Description"]


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

    createSkillWithLongDesc = client.post("/skills/", json={
        "Skill_Name": "Long name",
        "Skill_Description": "...........................................................................................................................................................................",
        "Active": True
    })
    assert createSkillWithLongDesc.json()["success"] == False


def test_view_available_skills():
    beforeAllSkills = len(client.get("/skills/").json()["data"])
    beforeAvailableSkills = len(client.get(
        "/skills/available/").json()["data"])
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

# ======================================== Staff Tests ========================================


def test_get_existing_staff():
    getExistingByID = client.post("/staff/one", json={"Staff_ID": "140001g"})
    # assert getExistingByID.json() == None
    assert getExistingByID.json()["success"] == True

    getNonExistingByID = client.post("/staff/one", json={"Staff_ID": "random"})
    assert getNonExistingByID.json()["success"] == False

    getExistingByEmail = client.post(
        "/staff/one", json={"Email": "Derek.Tan@allinone.com.sg"})
    assert getExistingByEmail.json()["success"] == True


# ======================================== Role Skill Relation Tests ========================================
def test_add_role_skill_relation():
    addSkillsToRole = client.post("/roleskillrelations/", json={
        "Role_ID": 8,
        "Skills": [1, 2, 3]
    })
    assert addSkillsToRole.json()["success"]

    addRolesToSkill = client.post("/skillrolerelations/", json={
        "Skill_ID": 1,
        "Roles": [1, 2, 3]
    })
    assert addRolesToSkill.json()["success"]

    updateSkillsToRole = client.put("/roleskillrelations/{Role_ID}".format(Role_ID=2), json={
        "Skills": [10, 11, 12]
    })
    assert updateSkillsToRole.json()["success"]

    updateRolesToSkill = client.put("/skillrolerelations/{Skill_ID}".format(Skill_ID=2), json={
        "Roles": [10, 11, 12]
    })
    assert updateRolesToSkill.json()["success"]

    viewRelatedSkillsRoleExist = client.get(
        "/roleskillrelations/{Role_ID}".format(Role_ID=2))
    assert viewRelatedSkillsRoleExist.json()["success"] == True

    viewRelatedSkillsRoleDontExist = client.get(
        "/roleskillrelations/{Role_ID}".format(Role_ID=-1))
    assert viewRelatedSkillsRoleDontExist.json()["success"] == False

    viewRelatedRolesSkillExist = client.get(
        "/skillrolerelations/{Skill_ID}".format(Skill_ID=1))
    assert viewRelatedRolesSkillExist.json()["success"] == True

    viewRelatedSkillsRoleDontExist = client.get(
        "/skillrolerelations/{Skill_ID}".format(Skill_ID=-1))
    assert viewRelatedSkillsRoleDontExist.json()["success"] == False

# ======================================== Learning Journey Tests ========================================


def test_create_lj():
    createLearningJourney = client.post("/learningjourney/", json={
        "Staff_ID": 130001,
        "Courses": ["COR001", "COR002"],
        "Skills": [1, 2, 3],
        "Role_ID": 1
    })
    assert createLearningJourney.json()["success"]


def test_view_lj():
    viewAllLjs = client.get("/learningjourney/")
    assert viewAllLjs.json()["success"]

    viewExistingLJ = client.get(
        "/learningjourney/{LearningJourney_ID}/".format(LearningJourney_ID=1))
    assert viewExistingLJ.json()["success"]
    viewNonExistingLJ = client.get(
        "/learningjourney/{LearningJourney_ID}/".format(LearningJourney_ID=-1))
    assert viewNonExistingLJ.json()["success"] == False

    viewExistingStaffLJ = client.get(
        "/learningjourney/staff/{Staff_ID}".format(Staff_ID=130001))
    assert viewExistingStaffLJ.json()["success"]

    viewExistingStaffLJ = client.get(
        "/learningjourney/staff/{Staff_ID}".format(Staff_ID=-1))
    assert viewExistingStaffLJ.json()["success"] == False


def delete_lj():
    deleteExistingLJ = client.delete(
        "/learningjourney/{LearningJourney_ID}/".format(LearningJourney_ID=1))
    assert deleteExistingLJ.json()["success"]
    deleteNonExistingLJ = client.delete(
        "/learningjourney/{LearningJourney_ID}/".format(LearningJourney_ID=-1))
    assert deleteNonExistingLJ.json()["success"] == False

# ======================================== Learning Journey Skill Relation Tests ========================================


def test_skill_to_lj():
    request = client.post("/learningjourneyskillrelation/",
                          json={
                              "LearningJourney_ID": 1,
                              "Skills": [1, 2, 3]
                          })
    assert request.json()["success"] == True

# ======================================== Course Skill Relation Tests ========================================


def test_add_skill_to_course():
    request = client.post("/courseskillrelations/", json={
        "Course_ID": "COR001",
        "Skills": [1, 2, 3]
    })
    assert request.json()["success"] == True


def test_update_skill_of_course():
    request = client.put("/courseskillrelations/{Course_ID}".format(Course_ID="FIN001"), json={
        "Skills": [10, 11, 12]
    })
    assert request.json()["success"] == True


def test_view_skills_of_course():
    request = client.get(
        "/courseskillrelations/{Course_ID}".format(Course_ID="FIN001"))
    assert request.json()["success"] == True


def test_view_course_by_skill_ids():
    request = client.post("/skillcourserelations/byid", json={
        "Skills": [1, 2, 3]
    })
    assert request.json()["success"] == True

# ======================================== Course Learning Journey Relation Tests ========================================


def test_add_course_lj():
    request = client.post("/courselearningjourney/",
                          json={
                              "LearningJourney_ID": 1,
                              "Courses": ["COR001", "COR002", "COR006"]
                          })
    assert request.json()["success"] == True


def test_delete_course_lj():
    allCourses = client.get("/course/").json()["data"]
    courseToAdd = allCourses[0]["Course_ID"]
    addedRowReq = client.post("/learningjourney/",
                              json={
                                  "Staff_ID": 130001,
                                  "Courses": [courseToAdd],
                                  "Role_ID": 21,
                                  "Skills": []}
                              )
    addedRow = addedRowReq.json()["data"]
    

    deleteWhenOneLeft = client.post("/courselearningjourney/delete",
                                    json={
                                        "LearningJourney_ID": addedRow,
                                        "Course_ID": courseToAdd
                                    })
    assert deleteWhenOneLeft.json()["success"] == False

    
    coursesToAdd = []
    for course in allCourses:
        coursesToAdd.append(course["Course_ID"])
    addedRowReq = client.post("/learningjourney/",
                              json={
                                  "Staff_ID": 130001,
                                  "Courses": coursesToAdd,
                                  "Role_ID": 21,
                                  "Skills": []}
                              )
    addedRow = addedRowReq.json()["data"]
    
    deleteWhenMoreThanOneLeft = client.post("/courselearningjourney/delete",
                                            json={
                                                "LearningJourney_ID": addedRow,
                                                "Course_ID": "COR001"
                                            })
    assert deleteWhenMoreThanOneLeft.json()["success"] == True
