from fastapi import FastAPI, APIRouter
from os import getenv
from dotenv import load_dotenv
# ============this loads the environment variables from .env============
load_dotenv()

# this retrieves the database URL from .env file
tags_metadata = [
    {
        "name": "HealthCheck",
        "description": "To check if the API is running correctly"
    },

    {
        "name": "SeedAll",
        "description": "Operations related to the seeding of data"
    },
    {
        "name": "DeleteAll",
        "description": "Operations related to the clearing of data"
    },
    {
        "name": "Roles",
        "description": "Operations related to the Role entity"
    },
    {
        "name": "Staff",
        "description": "Operations related to the Staff entity"
    },
    {
        "name": "Skills",
        "description": "Operations related to the Skills entity"
    },
    {
        "name": "Course",
        "description": "Operations related to the Course entity"
    },
    {
        "name": "LearningJourney",
        "description": "Operations related to the LearningJourney entity, which is unique to each user"
    },
    {
        "name": "RoleSkillRelations",
        "description": "Operations related to the RoleSkillRelations entity, which links Roles and Skills entities, but routes as skillrolerelations"
    },
    {
        "name": "SkillRoleRelations",
        "description": "Operations related to the RoleSkillRelations entity, which links Roles and Skills entities, but routes as roleskillrelations"
    },
    {
        "name": "CourseSkillRelation",
        "description": "Operations related to the CourseSkillRelation entity, which links Skills and Courses entities"
    },
    {
        "name": "CourseLearningJourney",
        "description": "Operations related to the CourseLearningJourney entity,which links Courses and LearningJourney entities"
    },
    {
        "name": "UserRoles",
        "description": "To assign staff with their system roles"
    },

]
database_route = getenv("DATABASE_URL")
# instantiate the FasAPI app
app = FastAPI(
    title="SPM G5T4 Backend",
    openapi_tags=tags_metadata,
    # root_path="/dev/"
      # when making pushes nid this line
)
# adding of middleware
temp = APIRouter()
# app = FastAPI()
