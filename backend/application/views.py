from django.shortcuts import render
from .serializers import *
from rest_framework import viewsets
from .models import *

# Create your views here.

class LecturerView(viewsets.ModelViewSet):
    queryset = Lecturer.objects.all()
    serializer_class = LecturerSerializer
    