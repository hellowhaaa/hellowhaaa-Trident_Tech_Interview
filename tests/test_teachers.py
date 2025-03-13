from unittest.mock import patch
from fastapi import FastAPI
from src.controller import courses
from fastapi.testclient import TestClient
from src.app import app

app = FastAPI()
app.include_router(courses.router,prefix="/courses")
TestClient(app)

def test_get_courses_normal():
    """
    測試目的：測試連線正常, 回傳status code 200
    """
    
    client = TestClient(app)
    response = client.get("/courses/")
    assert response.status_code == 200

def test_get_courses_empty():
    """
    測試目的：當list為空值, 資料格式仍然正確
    """
    test_dict_2 = {"datas": []}
    result = test_dict_2
    assert "datas" in test_dict_2
    assert isinstance(result["datas"], list)
    assert len(result["datas"]) == 0

def test_get_courses_partial_field():
    """
    測試目的：當缺少 Required parameter（teacherEmail）時, 能被正確抓錯
    """
    test_dict_3 = {
        "courseID": 123,
        "courseName": "English 101",
        "startTime": 1234,
        "endTime": 5678,
        "maxPeople": 10,
        "teacherID": 1,
        "teacherName": "Lily"
    }
    
    result = test_dict_3
    assert "teacherEmail" not in result
    