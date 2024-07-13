from rest_framework import serializers
from .models import User
from dj_rest_auth.registration.serializers import RegisterSerializer
from dj_rest_auth.serializers import UserDetailsSerializer

class CustomRegisterSerializer(serializers.ModelSerializer):
    class Meta(RegisterSerializer):
        model = User
        fields = (
            "email",
            "username",
            "phone_number",
            "role",
            "password",
            )
        
class CustomUserDetailsSerializer(UserDetailsSerializer):
    role = serializers.ReadOnlyField()
    class Meta():
        model = User
        fields = (
            "first_name",
            "last_name",
            "email",
            "username",
            "phone_number",
            "role",
            "profile_image",
        )