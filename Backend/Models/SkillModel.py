from typing import Optional
from datetime import datetime
from sqlmodel import Field, SQLModel

class Skill(SQLModel,table=True):
    __tablename__: "skill"
    SkillId: Optional[int] = Field(default=None, primary_key=True)
    SkillName: str
    SkillDescription: str
    Active: Bool
