from fastapi import APIRouter
from src.schemas.teachers import TeachersResponse, TeacherCoursesResponse, CreateTeacherRequest, CreateTeacherResponse
from src.schemas.courses import CreateCourseResponse, CreateCourseRequest
router = APIRouter()

@router.get("/", response_model=TeachersResponse)
def teachers():
    return {
        "datas":[
                {
                    "teacherID":123,
                    "name": "Ben",
                    "email": "Ben123@gamil.com"
                },
                {
                    "teacherID":456,
                    "name": "Nana",
                    "email": "Nana@gamil.com",
                }
            ]
        }

@router.get("/{teacher_id}/courses", response_model=TeacherCoursesResponse)
def teacher_courses():
    return {
	"datas":[
                {
                "courseID":123,
                "courseName": "Improve your math!",
                "startTime": 124343,
                "endTime": 789,
                "maxPeople": 10
                }
	    ]
    }

@router.post("/teachers", response_model=CreateTeacherResponse)
def create_teacher(r:CreateTeacherRequest):
    return {
		"teacherID":123, 
		"name": "Ben",
		"email": "Ben123@gamil.com",
	}

@router.post("/{teacher_id}/courses", response_model=CreateCourseResponse)
def create_course(r:CreateCourseRequest):
    return {
		"courseID":123,
		"courseName": "Improve your math!",
		"startTime": 124343,
		"endTime": 789,
		"maxPeople": 10,
		"teacherID": 123
	}


