
from config import app, prefix_router
# routes of independent entities
from Routes.Independent.CourseRoutes import *
from Routes.Independent.SkillRoutes import *
from Routes.Independent.RoleRoutes import *
from Routes.Independent.UserRoleRoutes import *

# routes of dependent entities
from Routes.Dependent.CourseSkillRelationRoutes import *
from Routes.Dependent.RoleSkillRelationRoutes import *
from Routes.Dependent.SkillRoleRelationRoutes import *
from Routes.Dependent.StaffRoutes import *
from Routes.Dependent.LearningJourneyRoutes import *
from Routes.Dependent.CourseLearningJourneyRoutes import *
from Routes.Dependent.SkillCourseRelationRoutes import *
from Routes.Dependent.LearningJourneySkillRoutes import *

from HelperFunctions import *
from ErrorHandler import *
from mangum import Mangum
from fastapi.middleware.cors import CORSMiddleware
from fastapi.routing import APIRouter


# Add the paths to the router instead
@prefix_router.get("/paths")
def service( request : Request ):
    return { "message" : request.scope.get("root_path")}

# Now add the router to the app
app.include_router(prefix_router)

@app.get("/",tags=["HealthCheck"])
async def healthCheck(request: Request):
    return {"message": "Hello World", "root_path": request.scope.get("root_path")}


origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

handler = Mangum(app)
