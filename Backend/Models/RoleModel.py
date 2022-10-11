from typing import Optional
from datetime import datetime
from sqlmodel import Field, SQLModel


class RoleModel(SQLModel,table=True):
    __tablename__: "rolemodel"
    Role_ID: Optional[int] = Field(default=None, primary_key=True)
    Role_Name:str
    Role_Description:str
    Active:bool