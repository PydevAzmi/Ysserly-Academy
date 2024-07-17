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
        fields = [
            "id",
            "user",
            "university",
            "college",
            "specialist",
            "bio",
        ]

