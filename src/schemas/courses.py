from src.schemas.base_model import Base
from pydantic import Field, EmailStr
from typing import List


class Course(Base):
    CourseID: int = Field(example=123, alias="courseID")
    CourseName: str = Field(example="Improve your English", alias="courseName")
    StartTime: int = Field(example=1234, alias="startTime")
    EndTime: int = Field(example=1234, alias="endTime")
    MaxPeople: int = Field(example=10, alias="maxPeople")


class CoursesTeacher(Course):
    TeacherID: int = Field(example=123, alias="teacherID")
    TeacherName: str = Field(example="Lily", alias="teacherName")
    TeacherEmail: EmailStr = Field(example="Lily@gmail.com", alias="teacherEmail")


class CreateCourseRequest(Base):
    CourseName: str = Field(example="Improve your English", alias="courseName")
    StartTime: int = Field(example=1234, alias="startTime")
    EndTime: int = Field(example=1234, alias="endTime")
    MaxPeople: int = Field(example=10, alias="maxPeople")
    TeacherID: int = Field(example=1234, alias="teacherID")


class CreateCourseResponse(Course):
    TeacherID: int = Field(example=1234, alias="teacherID")


class CoursesResponse(Base):
    Datas: List[CoursesTeacher] = Field(alias="datas")


