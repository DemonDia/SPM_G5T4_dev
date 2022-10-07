
from config import app
from Routes.RoleRoutes import *
from Routes.SkillRoutes import *
from HelperFunctions import *
from ErrorHandler import *
from mangum import Mangum
from fastapi.middleware.cors import CORSMiddleware



@app.get("/")
async def hello():
    return "OK"


origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

handler = Mangum(app)