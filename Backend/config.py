from fastapi import FastAPI
from os import getenv
from dotenv import load_dotenv
# ============this loads the environment variables from .env============
load_dotenv()

# this retrieves the database URL from .env file 
database_route = getenv("DATABASE_URL")
# instantiate the FasAPI app
app = FastAPI(
    # root_path="/dev/"
)
# adding of middleware
