from rest_framework import generics, filters
from .serializers import *
from .models import *
from django_filters.rest_framework import DjangoFilterBackend

class ProfessorListApiView(generics.ListAPIView):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['bio',"user__username", "specialist", ]
    filterset_fields = ['university','college']
    ordering_fields = ['university',]  

class ProfessorRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer


class CoursesListAPIView(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['description', "professor__user__first_name", "professor__user__last_name" , "specialist", ]
    filterset_fields = ['university','college']
    ordering_fields = ['university',]  

class CourseRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class LecturesListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = LectureSerialiazer
    def get_queryset(self):
        pk = self.kwargs["course_pk"]
        course = Course.objects.get(id=pk)
        queryset = Lecture.objects.filter(course = course)
        return queryset

    def perform_create(self, serializer):
        pk = self.kwargs["course_pk"]
        course = Course.objects.get(id=pk)
        serializer.save(course=course)


class LectureRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = LectureSerialiazer
    queryset = Lecture.objects.all()