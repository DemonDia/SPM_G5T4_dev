from typing import List,Optional
from sqlmodel import Field, SQLModel,Relationship
from Models.IndependentModels import *

class RoleSkillRelationModel(SQLModel, table=True):
    __tablename__: "roleskillrelationmodel"
    Role_ID: Optional[int] = Field(
        default=None, foreign_key="rolemodel.Role_ID", primary_key=True
    )
    Skill_ID: Optional[int] = Field(
        default=None, foreign_key="skillmodel.Skill_ID", primary_key=True
    )


class CourseSkillRelationModel(SQLModel, table=True):
    __tablename__: "courseskillrelationmodel"
    Course_ID: Optional[str] = Field(
        default=None, foreign_key="coursemodel.Course_ID", primary_key=True
    )
    Skill_ID: Optional[int] = Field(
        default=None, foreign_key="skillmodel.Skill_ID", primary_key=True
    )


class StaffModel(SQLModel, table=True):
    __tablename__: "staffmodel"
    Staff_ID: Optional[int] = Field(default=None, primary_key=True)
    Staff_FName: str
    Staff_LName: str
    Dept: str
    Email: str
    Role: Optional[int] = Field(
        default=None, foreign_key="userrolemodel.Role_ID")


class CourseLearningJourneyModel(SQLModel, table=True):
    __tablename__: "courselearningjourneymodel"
    Course_ID: Optional[str] = Field(
        default=None, foreign_key="coursemodel.Course_ID", primary_key=True)
    LearningJourney_ID: Optional[int] = Field(
        default=None, foreign_key="learningjourneymodel.LearningJourney_ID", primary_key=True)


class LearningJourneySkillRelationModel(SQLModel, table=True):
    __tablename__: "learningjourneyskillrelationmodel"
    LearningJourney_ID: Optional[int] = Field(
        default=None, foreign_key="learningjourneymodel.LearningJourney_ID", primary_key=True)
    Skill_ID: Optional[int] = Field(
        default=None, foreign_key="skillmodel.Skill_ID", primary_key=True
    )

class LearningJourneyModel(SQLModel, table=True):
    __tablename__: "learningjourneymodel"
    LearningJourney_ID: Optional[int] = Field(default=None, primary_key=True)
    Staff_ID: Optional[int] = Field(
        default=None, foreign_key="staffmodel.Staff_ID")
    Role_ID: Optional[int] = Field(
        default=None, foreign_key="rolemodel.Role_ID")

    Skills: List['SkillModel'] = Relationship(back_populates="LearningJourney", link_model=LearningJourneySkillRelationModel)
    Courses: List['CourseModel'] = Relationship(back_populates="LearningJourney", link_model=CourseSkillRelationModel)
