from typing import List, Optional
from sqlmodel import Field, SQLModel,Relationship
from Models.DependentModels import *

class CourseModel(SQLModel,table=True):
    __tablename__: "coursemodel"
    Course_ID: Optional[str] = Field(default=None, primary_key=True)
    Course_Name: str
    Course_Desc: str
    Course_Status: str
    Course_Type: str
    Course_Category: str
    Skills: List['SkillModel'] = Relationship(back_populates="Courses", link_model=CourseSkillRelationModel)
    LearningJourneys: List[LearningJourneyModel] = Relationship(back_populates="Courses",link_model=LearningJourneyModel)
    

class SkillModel(SQLModel,table=True):
    __tablename__: "skillmodel"
    Skill_ID: Optional[int] = Field(default=None, primary_key=True)
    Skill_Name: str
    Skill_Description: str
    Active: bool
    Roles: List['RoleModel'] = Relationship(back_populates="Skills", link_model=RoleSkillRelationModel)
    Courses: List['CourseModel'] = Relationship(back_populates="Skills", link_model=CourseSkillRelationModel)
    LearningJourneys: List[LearningJourneyModel] = Relationship(back_populates="Skills",link_model=LearningJourneyModel)

class RoleModel(SQLModel,table=True):
    __tablename__: "rolemodel"
    Role_ID: Optional[int] = Field(default=None, primary_key=True)
    Role_Name:str
    Role_Description:str
    Active:bool
    Skills: List['SkillModel'] = Relationship(back_populates="Roles", link_model=RoleSkillRelationModel)
    LearningJourneys: List[LearningJourneyModel] = Relationship(back_populates="Roles",link_model=LearningJourneyModel)


class UserRoleModel(SQLModel,table=True):
    __tablename__: "userrolemodel"
    Role_ID: Optional[int] = Field(default=None, primary_key=True)
    Role_Name:str