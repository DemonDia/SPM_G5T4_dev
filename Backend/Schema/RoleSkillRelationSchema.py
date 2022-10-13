from datetime import datetime
from typing import Optional

from pydantic import BaseModel

class RoleSkillRelation(BaseModel):
    Role_ID: Optional[int] = None
    Skill_ID: Optional[int] = None