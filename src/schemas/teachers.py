from src.schemas.base_model import Base
from pydantic import Field, EmailStr
from typing import List
from src.schemas.courses import Course

class Teacher(Base):
    TeacherID: int = Field(example=123, alias="teacherID")
    Name: str = Field(example="Ben", alias="name")
    Email: EmailStr = Field(example="Ben123@gmail.com", alias="email")

class TeachersResponse(Base):
    Datas: List[Teacher] = Field(alias="datas")

class TeacherCoursesResponse(Base):
    Datas: List[Course] = Field(alias="datas")

class CreateTeacherRequest(Base):
    Name: str = Field(example="Ben", alias="name")
    Email: EmailStr = Field(example="Ben123@gmail.com", alias="email")
    Password: str = Field(example="password123", alias="password")

class CreateTeacherResponse(Base):
    TeacherID: int = Field(example=43690, alias="teacherID")
    Name: str = Field(example="Ben", alias="name")
    Email: EmailStr = Field(example="Ben123@gmail.com", alias="email")