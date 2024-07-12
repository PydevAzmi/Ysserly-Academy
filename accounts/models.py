from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

def profile_image_path(instance, file_name):
    return f'images/users/{instance.username}/{file_name}'

ROLE = {
    ("Student","Student"),
    ("Prof","Professor "),
    }

class User(AbstractUser):
    email = models.EmailField(max_length=254, unique=True)
    role = models.CharField(_("role"), max_length=50, choices=ROLE)
    phone_number = models.CharField( max_length=14, null=True,blank=True)
    profile_image = models.ImageField(upload_to=profile_image_path, null=True,blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'phone_number']

