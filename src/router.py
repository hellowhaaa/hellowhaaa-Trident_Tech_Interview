
from fastapi import APIRouter
from src.controller import home, courses, teachers
router = APIRouter()

router.include_router(home.router)
router.include_router(courses.router, prefix="/courses")
router.include_router(teachers.router, prefix="/teachers")