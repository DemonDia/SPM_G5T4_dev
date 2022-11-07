from typing import Optional, List
from pydantic import BaseModel
from IndependentSchema import *

class CourseSkillRelation(BaseModel):
    Course_ID: Optional[str] = None
    Skill_ID: Optional[int] = None

class RoleSkillRelation(BaseModel):
    Role_ID: Optional[int] = None
    Skill_ID: Optional[int] = None


class Staff(BaseModel):
    Staff_ID: Optional[int] = None
    Staff_FName: str
    Staff_LName: str
    Dept: str
    Email: str
    Role: Optional[int] = None

class LearningJourney(BaseModel):
    LearningJourney_ID: Optional[int] = None
    Staff_ID: Optional[int] = None
    Role_ID: Optional[int] = None
    Skills: List[Skill]

class CourseLearningJourneyModel(BaseModel):
    Course_ID: Optional[str] = None
    LearningJourney_ID: Optional[int] = None

class LearningJourneySkill(BaseModel):
    LearningJourney_ID: Optional[int] = None
    Skill_ID: Optional[str] = None