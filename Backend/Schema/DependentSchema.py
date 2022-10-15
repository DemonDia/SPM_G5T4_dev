from datetime import datetime
from typing import Optional

from pydantic import BaseModel

class CourseSkillRelation(BaseModel):
    Course_ID: Optional[str] = None
    Skill_ID: Optional[int] = None

class RoleSkillRelation(BaseModel):
    Role_ID: Optional[int] = None
    Skill_ID: Optional[int] = None