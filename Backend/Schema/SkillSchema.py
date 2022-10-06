from datetime import datetime
from typing import Optional

from pydantic import BaseModel

class SkillSchema(BaseModel):
    SkillId: Optional[int] = Field(default=None, primary_key=True)
    skill_name: str
    skill_description: str
    Active: bool
