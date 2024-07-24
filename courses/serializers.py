from rest_framework import serializers
from accounts.models import User
from .models import *

class UserSerailizer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "first_name",
            "last_name",
            "username",
            "email",
            "phone_number",
            "profile_image",
        ]

class ProfessorSerializer(serializers.ModelSerializer):
    user = UserSerailizer(read_only=True)
    class Meta:
        model = Professor
        fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
    user = UserSerailizer(read_only=True)
    class Meta:
        model = Student
        fields= "__all__"

class CourseSerializer(serializers.ModelSerializer):
    professor = serializers.SerializerMethodField()
    is_enrolled = serializers.SerializerMethodField()
    is_requested = serializers.SerializerMethodField()
    enrolled_students = serializers.SerializerMethodField()
    class Meta:
        model = Course
        fields= "__all__"

    def get_professor(self, obj):
        return f"{obj.professor.user.first_name} {obj.professor.user.last_name}"
    
    def get_is_enrolled(self, obj):
        user = self.context['request'].user
        if not user.is_anonymous:
            if user.role == "Student":
                enrolled = Enrollment.objects.filter(course = obj, student = user.student_profile).exists()
                return True if enrolled else False
        return False
    
    def get_enrolled_students(self, obj):
        return Enrollment.objects.filter(course = obj).count()
    
    def get_is_requested(self, obj):
        user = self.context["request"].user
        if user.role == "Student":
            requested = Request.objects.filter(course = obj, student = user.student_profile, status="Pending").exists()
            return True if requested else False
        return False

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model =FileContent
        fields = ["id", 'file', 'upload_date' ]

class VideosSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoContent
        fields = ["id", 'url', 'upload_date']

class LectureSerialiazer(serializers.ModelSerializer):
    course = serializers.SerializerMethodField()
    files = FileSerializer(read_only=True ,many=True)
    videos = VideosSerializer(many=True, read_only=True)
    class Meta:
        model = Lecture
        fields =[
            "id",
            "course",
            "title",
            "upload_date",
            "videos",
            "files",
        ]

    def get_course(self, obj):
        return f"{obj.course.title}"
    
class EnrollmentSerializer(serializers.ModelSerializer):
    student = StudentSerializer()
    class Meta:
        model = Enrollment
        fields = [
            "id",
            "student",
        ]


class RequestSerializer(serializers.ModelSerializer):
    student = serializers.SerializerMethodField()
    course = serializers.SerializerMethodField()
    #status = serializers.ReadOnlyField()
    class Meta:
        model = Request
        fields = '__all__'

    def get_course(self, obj):
        return f"{obj.course.title}"
        
    def get_student(self, obj):
        return f"{obj.student.user.username}"