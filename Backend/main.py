
from Models.TrackModel import TrackModel
from config import app
from Routes.TrackRoutes import *
from Routes.RoleRoutes import *
from Routes.SkillRoutes import *
from HelperFunctions import *
from ErrorHandler import *
from mangum import Mangum

@app.on_event("startup")
async def startup_event():
    seedInitialData("track",TrackModel)

@app.get("/")
async def hello():
    return "OK"
    
handler = Mangum(app)