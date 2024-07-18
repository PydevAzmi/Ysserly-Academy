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

class CourseSerializer(serializers.ModelSerializer):
    professor = serializers.SerializerMethodField()
    class Meta:
        model = Course
        fields= "__all__"

    def get_professor(self, obj):
        return f"{obj.professor.user.first_name} {obj.professor.user.last_name}"

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
    
        