from typing import Optional
from pydantic import BaseModel

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