from tkinter.tix import Tree
from typing import Optional
from sqlmodel import Field, SQLModel

class RoleSkillRelationModel(SQLModel,table=True):
    __tablename__: "roleskillrelationmodel"
    Role_ID: Optional[int] = Field(
        default=None, foreign_key="rolemodel.Role_ID", primary_key=True
    )
    Skill_ID: Optional[int] = Field(
        default=None, foreign_key="skillmodel.Skill_ID", primary_key=True
    )

class CourseSkillRelationModel(SQLModel,table=True):
    __tablename__: "courseskillrelationmodel"
    Course_ID: Optional[str] = Field(
        default=None, foreign_key="coursemodel.Course_ID", primary_key=True
    )
    Skill_ID: Optional[int] = Field(
        default=None, foreign_key="skillmodel.Skill_ID", primary_key=True
    )
class StaffModel(SQLModel,table=True):
    __tablename__: "staffmodel"
    Staff_ID: Optional[int] = Field(default=None, primary_key=True)
    Staff_FName: str
    Staff_LName: str
    Dept: str
    Email: str
    Role: Optional[int] = Field(default=None, foreign_key="userrolemodel.Role_ID") 

