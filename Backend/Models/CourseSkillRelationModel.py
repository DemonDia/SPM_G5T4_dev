from typing import Optional
from datetime import datetime
from sqlmodel import Field, SQLModel


class CourseSkillRelationModel(SQLModel,table=True):
    __tablename__: "courseskillrelationmodel"
    Course_ID: Optional[str] = Field(
        default=None, foreign_key="coursemodel.Course_ID", primary_key=True
    )
    Skill_ID: Optional[int] = Field(
        default=None, foreign_key="skillmodel.Skill_ID", primary_key=True
    )
