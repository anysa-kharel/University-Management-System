from django.shortcuts import render
from .serializers import *
from rest_framework import viewsets,status
from .models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.

class LecturerView(viewsets.ModelViewSet):
    queryset = Lecturer.objects.all()
    serializer_class = LecturerSerializer


class StudentView(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class ModuleView(viewsets.ModelViewSet):
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer


class LectureView(viewsets.ModelViewSet):
    queryset = Lecture.objects.all()
    serializer_class = LectureSerializer


class TutorView(viewsets.ModelViewSet):
    queryset = Tutor.objects.all()
    serializer_class = TutorSerializer

    # def post(self, request, *args, **kwargs):
    #     serializer = TutorSerializer(data=request.data, many =True)
    #     serializer.is_valid(raise_exception=True)
    #     validated_data = serializer._validated_data.pop()
        
    #     tutor_entry_data = validated_data['lecturer','student']
    #     tutor_entry_model = Tutor(**tutor_entry_data)
    #     tutor_entry_model.save()

    #     return Response({'message':'Success'})

class RegistrationView(viewsets.ModelViewSet):
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer