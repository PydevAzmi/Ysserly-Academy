from rest_framework import serializers
from allauth.account.adapter import get_adapter
from allauth.account.utils import setup_user_email
from .models import User, ROLE
from django.core.exceptions import ValidationError as DjangoValidationError
from dj_rest_auth.registration.serializers import RegisterSerializer
from dj_rest_auth.serializers import UserDetailsSerializer
from django.core.validators import MinLengthValidator, MaxLengthValidator


class CustomRegisterSerializer(RegisterSerializer):
    role = serializers.ChoiceField(choices=ROLE, required =True)
    phone_number = serializers.CharField(
        max_length=15, required=True,
        validators=[
            MinLengthValidator(10, message="Phone number must be at least 10 characters long."),
            MaxLengthValidator(15, message="Phone number must be at most 15 characters long.")
        ])

    def get_cleaned_data(self):
        data = super().get_cleaned_data()
        data['phone_number'] = self.validated_data.get('phone_number', '')
        data['role'] = self.validated_data.get('role', '')
        return data

    def save(self, request):
        user = super().save(request)
        user.phone_number = self.cleaned_data.get('phone_number')
        user.role = self.cleaned_data.get('role')
        user.save()
        return user
        
class CustomUserDetailsSerializer(UserDetailsSerializer):
    role = serializers.ReadOnlyField()
    class Meta():
        model = User
        fields = (
            "id",
            "first_name",
            "last_name",
            "email",
            "username",
            "phone_number",
            "role",
            "profile_image",
        )