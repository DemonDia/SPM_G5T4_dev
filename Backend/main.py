from Backend.Models.TrackModel import TrackModel
from Backend.config import app
from Backend.Routes.TrackRoutes import *
from Backend.HelperFunctions import *
from Backend.ErrorHandler import *
# instantiate the FasAPI app

@app.on_event("startup")
async def startup_event():
    seedInitialData("track",TrackModel)

@app.get("/")
async def hello():
    return "OK"