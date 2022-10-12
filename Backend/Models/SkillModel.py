from typing import Optional
from datetime import datetime
from sqlmodel import Field, SQLModel

class SkillModel(SQLModel,table=True):
    __tablename__: "skillmodel"
    Skill_ID: Optional[int] = Field(default=None, primary_key=True)
    Skill_Name: str
    Skill_Description: str
    Active: bool
