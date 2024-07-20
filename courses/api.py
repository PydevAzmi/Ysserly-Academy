from rest_framework import generics, filters
from .serializers import *
from .models import *
from .permissions import *
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
    ordering_fields = ['price',] 
    permission_classes = [ permissions.IsAuthenticated, IsProfessorOrReadOnly] 

    def perform_create(self, serializer):
        return serializer.save(professor=self.request.user.professor_profile)

class CourseRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [ permissions.IsAuthenticated, IsProfessorOrReadOnly] 


class LecturesListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = LectureSerialiazer
    permission_classes = [permissions.IsAuthenticated, Is_CourseOwnerOrStudentApproved]
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

class FilesListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = FileSerializer
    def get_queryset(self):
        pk = self.kwargs["lec_pk"]
        lec = Lecture.objects.get(id=pk)
        queryset = FileContent.objects.filter(lecture = lec)
        return queryset

    def perform_create(self, serializer):
        pk = self.kwargs["lec_pk"]
        lec = Lecture.objects.get(id=pk)
        serializer.save(lecture=lec)

class FileRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = FileSerializer
    queryset = FileContent.objects.all()


class VideosListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = VideosSerializer
    def get_queryset(self):
        pk = self.kwargs["lec_pk"]
        lec = Lecture.objects.get(id=pk)
        queryset = VideoContent.objects.filter(lecture = lec)
        return queryset

    def perform_create(self, serializer):
        pk = self.kwargs["lec_pk"]
        lec = Lecture.objects.get(id=pk)
        serializer.save(lecture=lec)

class videoRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = VideosSerializer
    queryset = VideoContent.objects.all()


class EnrollmentListAPIView(generics.ListAPIView):
    serializer_class = EnrollmentSerializer
    def get_queryset(self):
        pk = self.kwargs["course_pk"]
        course = Course.objects.get(id=pk)
        queryset = Enrollment.objects.filter(course = course)
        return queryset

class EnrollmentRetrieveUpdateDestroyAPIView(generics.RetrieveDestroyAPIView):
    serializer_class = EnrollmentSerializer
    queryset = Enrollment.objects.all()

class RequestListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = RequestSerializer
    permission_classes = [IsStudentOrReadOnly]
    def get_queryset(self):
        pk = self.kwargs["course_pk"]
        course = Course.objects.get(id=pk)
        queryset = Request.objects.filter(course = course, status="Pending")
        return queryset
    
    def perform_create(self, serializer):
        pk = self.kwargs["course_pk"]
        course = Course.objects.get(id=pk)
        user = self.request.user
        serializer.save(course=course, student=user.student_profile)
        return super().perform_create(serializer)


class RequestRetrieveUpdateDestroyAPIView(generics.RetrieveDestroyAPIView):
    serializer_class = RequestSerializer
    queryset = Request.objects.all()