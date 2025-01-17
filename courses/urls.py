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
    path("courses/<course_pk>/lectures/", LecturesListCreateAPIView.as_view(), name="lectures_list" ),
    path("courses/<course_pk>/lectures/<pk>/", LectureRetrieveUpdateDestroyAPIView.as_view(), name="lectures_instance" ),

    # Lecture's Fiels
    path("courses/<course_pk>/lectures/<lec_pk>/files/", FilesListCreateAPIView.as_view(), name="files_list" ),
    path("courses/<course_pk>/lectures/<lec_pk>/files/<pk>", FileRetrieveUpdateDestroyAPIView.as_view(), name="file_instance" ),

    # Lecture's Videos
    path("courses/<course_pk>/lectures/<lec_pk>/videos/", VideosListCreateAPIView.as_view(), name="video_list" ),
    path("courses/<course_pk>/lectures/<lec_pk>/videos/<pk>", videoRetrieveUpdateDestroyAPIView.as_view(), name="video_instance" ),

    # Students requests to course
    path("courses/<course_pk>/requests/", RequestListCreateAPIView.as_view(), name="requests_list" ),
    path("courses/<course_pk>/requests/<pk>/", RequestRetrieveUpdateDestroyAPIView.as_view(), name="request_instance" ),

    # Enrolled Students in course
    path("courses/<course_pk>/enrolled-students/", EnrollmentListAPIView.as_view(), name="enrolled_list" ),
    path("courses/<course_pk>/enrolled-students/<pk>/", EnrollmentRetrieveUpdateDestroyAPIView.as_view(), name="enrolled_instance" ),
]
