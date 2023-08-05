from django.shortcuts import render
from .serializers import *
from rest_framework import viewsets,status
from .models import *
from rest_framework.views import APIView
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

    def post(self, request, *args, **kwargs):
        tutors_data = request.data.get("tutors", [])
        
        if not isinstance(tutors_data, list):
            return Response(
                {"detail": "Invalid data format. 'tutors' should be a list."},
                status=status.HTTP_400_BAD_REQUEST
            )
            
        serializer = TutorSerializer(data=tutors_data, many=True)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RegistrationView(viewsets.ModelViewSet):
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer

# class DepartmentView(viewsets.ModelViewSet):
#     queryset = Department.objects.all()
#     serializer_class = DepartmentSerializer

class SemesterView(viewsets.ModelViewSet):
    queryset = Semester.objects.all()
    serializer_class = SemesterSerializer