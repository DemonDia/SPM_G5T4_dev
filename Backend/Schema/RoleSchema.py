from datetime import datetime
from typing import Optional

from pydantic import BaseModel

class Role(BaseModel):
    Role_ID: Optional[int] = None
    Role_Name:str
    Role_Description:str
    Active:bool