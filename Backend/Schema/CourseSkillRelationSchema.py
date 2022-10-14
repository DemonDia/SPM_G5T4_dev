from datetime import datetime
from typing import Optional

from pydantic import BaseModel

class CourseSkillRelation(BaseModel):
    Course_ID: Optional[str] = None
    Skill_ID: Optional[int] = None
    # Role_ID: Column(int, ForeignKey('tenant.tenant_id', ondelete='CASCADE'), primary_key=True)
