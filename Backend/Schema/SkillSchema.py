from datetime import datetime
from typing import Optional

from pydantic import BaseModel

class SkillSchema(BaseModel):
    SkillId: Optional[int] = Field(default=None, primary_key=True)
    SkillName: str
    SkillDescription: str
    Active: bool
