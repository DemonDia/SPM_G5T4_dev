from fastapi import FastAPI
from os import getenv
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware

# ============this loads the environment variables from .env============
load_dotenv()

# this retrieves the database URL from .env file 
database_route = getenv("DATABASE_URL")
# instantiate the FasAPI app
app = FastAPI()
# adding of middleware

# CORS 
origins = [
    "http://localhost:8081",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)