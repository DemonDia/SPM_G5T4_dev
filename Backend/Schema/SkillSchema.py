from datetime import datetime
from typing import Optional

from pydantic import BaseModel

class SkillSchema(BaseModel):
    Skill_ID: Optional[int] = None
    Skill_Name: str
    Skill_Description: str
    Active: bool
