from rest_framework import generics, filters
from .serializers import *
from .models import *
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
