from django.urls import path
from .api import *

urlpatterns = [
    # Professors
    path("professors/", ProfessorListApiView.as_view(), name="professor_list" ),
    path("professors/<pk>/", ProfessorRetrieveUpdateDestroyAPIView.as_view(), name="professor_instance" ),
    # Courses
    path("courses/", CoursesListAPIView.as_view(), name="courses_list" ),
    path("courses/<pk>/", CourseRetrieveUpdateDestroyAPIView.as_view(), name="courses_instance" ),
    # Course's Lectures
    path("courses/<course_pk>/lectures/", LecturesListCreateAPIView.as_view(), name="Lectures_list" ),
    path("courses/<course_pk>/lectures/<pk>/", LectureRetrieveUpdateDestroyAPIView.as_view(), name="Lectures_instance" ),
]
