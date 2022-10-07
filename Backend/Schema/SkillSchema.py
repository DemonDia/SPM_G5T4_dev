from datetime import datetime
from typing import Optional

from pydantic import BaseModel

class SkillSchema(BaseModel):
    id: Optional[int] = None
    skill_name: str
    skill_description: str
    Active: bool
