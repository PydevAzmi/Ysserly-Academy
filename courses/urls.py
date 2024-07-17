from django.urls import path
from .api import *

urlpatterns = [
    path("professors/", ProfessorListApiView.as_view(), name="professor_list" ),
    path("professors/<pk>/", ProfessorRetrieveUpdateDestroyAPIView.as_view(), name="professor_instance" ),
]
