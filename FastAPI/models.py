from enum import Enum
from uuid import UUID, uuid4
from pydantic import BaseModel
from typing import Optional,List

class Gender(str,Enum):
    male = "male"
    female = "female"

class Role(str,Enum):
    admin = "admin"
    user = "user"
    student = "student"

class User(BaseModel):
    id : Optional[UUID] = uuid4()
    firstName : str
    lastName : str
    middleName : Optional[str]
    gender : Gender
    role : List[Role]

class UserUpdateRequest(BaseModel):
    firstName :Optional[str]
    lastName :Optional[str]
    middleName :Optional[str]
    gender : Optional[Gender]
    role :Optional[List[Role]]