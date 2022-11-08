# from HelperFunctionForTest import cleanUp, seedAllData
# from TestScripts.Dependent.RoleSkillRelationTest import testAllRoleSkillRelationCases
# from TestScripts.Dependent.CourseSkillRelationTest import testAllCourseSkillRelationCases
# from TestScripts.Independent.RoleTest import testAllRoleCases
# from TestScripts.Independent.SkillTest import testAllSkillCases
# from TestScripts.Dependent.StaffTest import testAllStaffCases
# from TestScripts.Dependent.LearningJourneyTest import testAllLearningJourneyCases
# from TestScripts.Dependent.CourseLearningJourneyTest import testAllCourseLearningJourneyCases
# from TestScripts.Dependent.LearningJourneySkillTest import testAllLearningJourneySkillRelationCases
# import pytest

# @pytest.fixture(autouse=True)
# def start():
#     cleanUp()
#     seedAllData()
#     yield
#     # cleanUp()


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

# if __name__ == "__main__":
#     cleanUp()
#     seedAllData()
#     mainTest()
#     cleanUp()


# import logging
# from fastapi import FastAPI

# class App:
#     """ Core application to test. """

#     def __init__(self):
#         self.api = FastAPI()
#         # register endpoints
#         self.api.get("/")(self.read_root)
#         self.api.on_event("shutdown")(self.close)

#     async def close(self):
#         """ Gracefull shutdown. """
#         logging.warning("Shutting down the app.")

#     async def read_root(self):
#         """ Read the root. """
#         return {"Hello": "World"}

# """ Testing part."""
# from multiprocessing import Process
# import asynctest
# import asyncio
# import aiohttp
# import uvicorn

# class TestScriptApp(asynctest.TestCase):
#     """ Test the app class. """

#     async def setUp(self):
#         """ Bring server up. """
#         app = App()
#         self.proc = Process(target=uvicorn.run,
#                             args=(app.api,),
#                             kwargs={
#                                 "host": "127.0.0.1",
#                                 "port": 8000,
#                                 "log_level": "info"},
#                             daemon=True)
#         self.proc.start()
#         await asyncio.sleep(0.1)  # time for the server to start

#     async def tearDown(self):
#         """ Shutdown the app. """
#         self.proc.terminate()

#     async def test_read_root(self):
#         """ Fetch an endpoint from the app. """
#         async with aiohttp.ClientSession() as session:
#             cleanUp()
#             seedAllData()
#             mainTest()
#             cleanUp()


# ============================imports============================
# ===============test scripts===============
# from HelperFunctionForTest import cleanUp, seedAllData
# from TestScripts.Dependent.RoleSkillRelationTest import testAllRoleSkillRelationCases
# from TestScripts.Dependent.CourseSkillRelationTest import testAllCourseSkillRelationCases
# from TestScripts.Independent.RoleTest import testAllRoleCases
# from TestScripts.Independent.SkillTest import testAllSkillCases
# from TestScripts.Dependent.StaffTest import testAllStaffCases
# from TestScripts.Dependent.LearningJourneyTest import testAllLearningJourneyCases
# from TestScripts.Dependent.CourseLearningJourneyTest import testAllCourseLearningJourneyCases
# from TestScripts.Dependent.LearningJourneySkillTest import testAllLearningJourneySkillRelationCases

# from HelperFunctionForTest import cleanUp, seedAllData
# from TestScripts.Dependent.RoleSkillRelationTest import testAllRoleSkillRelationCases
# from TestScripts.Dependent.CourseSkillRelationTest import testAllCourseSkillRelationCases
# from Tests.TestScripts.Independent.RoleTest import testAllRoleCases
# from TestScripts.Independent.SkillTest import testAllSkillCases
# from TestScripts.Dependent.StaffTest import testAllStaffCases
# from TestScripts.Dependent.LearningJourneyTest import testAllLearningJourneyCases
# from TestScripts.Dependent.CourseLearningJourneyTest import testAllCourseLearningJourneyCases
# from TestScripts.Dependent.LearningJourneySkillTest import testAllLearningJourneySkillRelationCases
# import pytest


# ===============test client===============
from fastapi.testclient import TestClient
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


# ============================FastAPI test============================
client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200

# def test_health_check():
#     response = client.get("/docs")
#     print(response)
#     assert response.status_code == 200

def test_get_roles():
    response = client.get("/roles/")
    assert response.status_code == 200

def test_post_roles():
    createRole = client.post("/roles/",
                             {
                                 "Role_Name": "Product Manager",
                                 "Role_Description": "Product Manager needs to collaborate effectively with cross-functional stakeholders to create a smooth user experience for job seekers and employers",
                                 "Active": True
                             })
    print(createRole)
    assert createRole.status_code == 200

