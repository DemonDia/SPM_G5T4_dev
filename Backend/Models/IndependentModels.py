from typing import List, Optional
from datetime import datetime
from sqlmodel import Field, SQLModel,Relationship
from Models.RoleSkillRelationModel import RoleSkillRelationModel


class SkillModel(SQLModel,table=True):
    __tablename__: "skillmodel"
    Skill_ID: Optional[int] = Field(default=None, primary_key=True)
    Skill_Name: str
    Skill_Description: str
    Active: bool
    Roles: List['RoleModel'] = Relationship(back_populates="Skills", link_model=RoleSkillRelationModel)

class RoleModel(SQLModel,table=True):
    __tablename__: "rolemodel"
    Role_ID: Optional[int] = Field(default=None, primary_key=True)
    Role_Name:str
    Role_Description:str
    Active:bool
    Skills: List['SkillModel'] = Relationship(back_populates="Roles", link_model=RoleSkillRelationModel)



