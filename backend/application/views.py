from django.shortcuts import render
from .serializers import *
from rest_framework import viewsets,status
from django.http import Http404
from .models import *
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.

@api_view(['GET', 'POST'])
def lecturer_list(request):

    if request.method == 'GET':
        lecturer = Lecturer.objects.all()
        serializer = LecturerSerializer(lecturer, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = LecturerSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

   
@api_view(['GET','PUT','DELETE'])
def lecturer_detail(request, pk):

    try:
        lecturer = Lecturer.objects.get(id=pk)
    except Lecturer.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = LecturerSerializer(lecturer)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = LecturerSerializer(lecturer, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        lecturer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def student_list(request):

    if request.method == 'GET':
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = StudentSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET','PUT','DELETE'])
def student_detail(request, pk):

    try:
        student = Student.objects.get(student_id=pk)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = StudentSerializer(student)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = StudentSerializer(student, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ModuleView(viewsets.ModelViewSet):
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer


class LectureView(viewsets.ModelViewSet):
    queryset = Lecture.objects.all()
    serializer_class = LectureSerializer


class TutorView(viewsets.ModelViewSet):
    queryset = Tutor.objects.all()
    serializer_class = TutorSerializer


class RegistrationView(viewsets.ModelViewSet):
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer


class SemesterView(viewsets.ModelViewSet):
    queryset = Semester.objects.all()
    serializer_class = SemesterSerializer



@api_view(['GET', 'POST'])
def semester_list(request):

    if request.method == 'GET':
        semester = Semester.objects.all()
        serializer = SemesterSerializer(semester, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = SemesterSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def semester_detail(request ,pk):

    try:
        faculty = Semester.objects.filter(faculty=pk)

    except Semester.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = SemesterSerializer(faculty, many = True)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = SemesterSerializer(faculty, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        serializer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET','PUT','DELETE'])
def semester_details(request,faculty ,pk):

    try:
        semester = Semester.objects.filter(faculty = faculty, sem=pk)

    except Semester.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = SemesterSerializer(semester, many = True)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = SemesterSerializer(semester, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        serializer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

@api_view(['GET', 'POST'])
def form_list(request):

    if request.method == 'GET':
        form = Form.objects.all()
        serializer = FormSerializer(form, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = FormSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def form_details(request ,pk):

    try:
        form = Form.objects.filter(id = pk)

    except Form.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = FormSerializer(form, many = True)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = FormSerializer(form, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        serializer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)












    # class LecturerView(viewsets.ModelViewSet):
#     queryset = Lecturer.objects.all()
#     serializer_class = LecturerSerializer

#     def get_object(self,pk):
#         try:
#             return Lecturer.objects.get(id=pk)
#         except Lecturer.DoesNotExist:
#             raise Http404


#     def get(self,request, pk, format = None):
#         lecturers = self.get_object(pk)
#         serializer = LecturerSerializer(lecturers)
#         return Response(serializer.data)
    

#     def put(self,request,pk=None,format = None):
#         lecturers = self.get_object(pk)
#         serializer =LecturerSerializer(lecturers, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     def delete(self,request,pk,format = None):
#         lecturers = self.get_object(pk)
#         lecturers.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
