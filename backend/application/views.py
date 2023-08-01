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

    # def create(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data = request.data)
    #     if serializer.is_valid():
    #         if lecturer_number_exists(request.data['lecturer_number']):
    #             return Response({'error': 'Lecturer number already exists'}, status=status.HTTP__400_BAD_REQUEST)
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
    

    # def update(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     serializer = self.get_serializer(instance, data = request.data)
        
    #     if serializer.is_valid():
    #         if lecturer_number_exists(request.data['lecturer_number']):
    #             return Response({"error": "Lecturer with this lecturer number already exists."}, status=status.HTTP_400_BAD_REQUEST)

    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_200_OK)

    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StudentView(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    # def create(self, request, *args, **kwargs):
    #     student_data = request.data
    #     valid_students =[]

    #     for student_data in student_data:
    #         serializer = self.get_serializer(data=student_data)
    #         if serializer.is_valid():
    #             serializer.save()
    #         else:
    #             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ModuleView(viewsets.ModelViewSet):
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer