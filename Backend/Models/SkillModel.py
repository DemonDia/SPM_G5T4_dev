from typing import Optional
from datetime import datetime
from sqlmodel import Field, SQLModel

class SkillModel(SQLModel,table=True):
    __tablename__: "skillmodel"
    SkillId: Optional[int] = Field(default=None, primary_key=True)
    skill_name: str
    skill_description: str
    Active: bool
