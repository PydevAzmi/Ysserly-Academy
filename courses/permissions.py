from rest_framework import permissions
from .models import *

class IsProfessorOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.role == 'Professor'
    
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.professor == request.user.professor_profile

class IsStudentOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.role == 'Student'
    
    def has_object_permission(self, request, view, obj):
        if request.user.role == 'Professor':
            if request.method in ('GET', 'HEAD', 'OPTIONS', 'patch'):
                return obj.course.professor == request.user.professor_profile
            return False
        return obj.student == request.user.student_profile

class IsStudentAndApproved(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.role != 'student':
            return False
        enrollment = Enrollment.objects.filter(student=request.user.student_profile, course=view.kwargs['course_pk']).exists()
        return enrollment is not None

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user
    

class Is_CourseOwnerOrStudentApproved(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.role != 'Student': 
            return False
        
        enrolled = Enrollment.objects.filter(student=request.user.student_profile, course=view.kwargs['course_pk']).exists()
        return True if enrolled else False
    
    def has_object_permission(self, request, view, obj):
        user = request.user
        if request.method in permissions.SAFE_METHODS:
            if user.role=="Student" and user.student_profile in  obj.course.enrollments.student.all():
                return True
            return False
        return obj.course.professor == user.professor_profile
    
    