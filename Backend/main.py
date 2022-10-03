from Models.TrackModel import TrackModel # requires Backend.
from config import app # requires Backend.
from Routes.TrackRoutes import * # requires Backend.
from HelperFunctions import * # requires Backend.
from ErrorHandler import * # requires Backend.

# instantiate the FastAPI app

@app.on_event("startup")
async def startup_event():
    seedInitialData("track",TrackModel)

@app.get("/")
async def hello():
    return "OK"