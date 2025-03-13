from fastapi import APIRouter
from src.schemas.courses import CreateCourseRequest, CreateCourseResponse, CoursesResponse, Course

router = APIRouter()

@router.get("/")
def all_courses():
    return { 
        "datas":[
            {
                "courseID": 123,
                "courseName": "Improve your English",
                "startTime": 124343,
                "endTime": 789,
                "maxPeople": 10,
                "teacherID":123,
                "teacherName": "Lily",
                "teacherEmail": "Lily@gamil.com",
            }
	    ]
    }

@router.put("/{course_id}", response_model=CreateCourseResponse)
def course(r: CreateCourseRequest):
    return {
		"courseID":123, 
		"courseName": "Improve your math!",
		"startTime": 124343,
		"endTime": 789,
		"maxPeople": 10,
		"teacherID": 123
	}

@router.delete("/{course_id}", response_model=Course)
def delete_course():
    return {
		"courseID":123, 
		"courseName": "Improve your math!",
		"startTime": 124343,
		"endTime": 789,
		"maxPeople": 10
	}




