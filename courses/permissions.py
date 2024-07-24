from rest_framework import permissions
from .models import *
from django.shortcuts import get_object_or_404

class IsProfessorOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.role == 'Professor'
    
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.professor == request.user.professor_profile

class IsStudentOrProfessorResponse(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.role == "Student":
            requested = Request.objects.filter(student=request.user.student_profile, course=view.kwargs['course_pk']).exists()
            if not requested or request.method in ('GET', 'HEAD', 'OPTIONS', 'DELETE'):
                return True
            return False
        else:
            course = get_object_or_404(Course, pk = view.kwargs['course_pk'])
            if request.user == course.professor.user:
                if request.method in ('GET', 'HEAD', 'OPTIONS', 'PUT','DELETE'):
                    return True
            return False

class Is_CourseOwnerOrStudentApproved(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.role == 'Student': 
            if request.method in permissions.SAFE_METHODS:
                enrolled = Enrollment.objects.filter(student=request.user.student_profile, course=view.kwargs['course_pk']).exists()
                return True if enrolled else False
            return False
        else:
            course=Course.objects.get(id = view.kwargs['course_pk'])
            if request.user == course.professor.user:
                return True
        return False
    