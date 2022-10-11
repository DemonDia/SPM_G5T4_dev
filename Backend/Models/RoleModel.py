from typing import Optional
from datetime import datetime
from sqlmodel import Field, SQLModel


class RoleModel(SQLModel,table=True):
    __tablename__: "rolemodel"
    id: Optional[int] = Field(default=None, primary_key=True)
    role_name:str
    role_description:str
    active:bool