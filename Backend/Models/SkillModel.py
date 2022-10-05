from typing import Optional
from datetime import datetime
from sqlmodel import Field, SQLModel

class SkillModel(SQLModel,table=True):
    __tablename__: "skillmodel"
    SkillId: Optional[int] = Field(default=None, primary_key=True)
    SkillName: str
    SkillDescription: str
    Active: bool
