from datetime import datetime
from typing import Optional, List

from pydantic import BaseModel


class Role(BaseModel):
    Role_ID: Optional[int] = None
    Role_Name: str
    Role_Description: str
    Active: bool
    Skills: List["SkillSchema"]
    # Skills:


class SkillSchema(BaseModel):
    Skill_ID: Optional[int] = None
    Skill_Name: str
    Skill_Description: str
    Active: bool
    Roles: List[Role]
