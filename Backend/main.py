from config import app
from Routes.TrackRoutes import *
from HelperFunctions import *
from ErrorHandler import *
# instantiate the FasAPI app



@app.get("/")
async def hello():
    return "OK"