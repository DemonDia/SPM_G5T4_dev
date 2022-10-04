from datetime import datetime
from typing import Optional

from pydantic import BaseModel

class Role(BaseModel):
    id: Optional[int] = None
    role_name:str
    role_description:str
    active:bool