from django.shortcuts import render
from .serializers import *
from rest_framework import viewsets,status
from django.http import Http404
from .models import *
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.
class LecturerView(viewsets.ModelViewSet):
    queryset = Lecturer.objects.all()
    serializer_class = LecturerSerializer

    # def get_object(self,pk):
    #     try:
    #         return Lecturer.objects.get(pk=pk)
    #     except Lecturer.DoesNotExist:
    #         raise Http404


    # def get(self,request, pk = None, format = None):
    #     lecturers = self.get_object(pk)
    #     serializer = LecturerSerializer(lecturers)
    #     return Response(serializer.data)
    

    # def put(self,request,pk,format = None):
        
    #     lecturers = self.get_object(pk)
    #     serializer =LecturerSerializer(lecturers, data=request.data, partial = True )
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk = None,format = None):
        lecturers = self.get_object(pk)
        lecturers.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    @api_view(['GET','POST'])
    def lecturer_detail(request,pk, format = None):
        try:
            lecturer = Lecturer.objects.get(pk)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        if request.method == 'GET':
            serializer = LecturerSerializer(lecturer)
            return Response(serializer.data)

        elif request.method == 'PUT':
            serializer =LecturerSerializer(lecturer, data=request.data)
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
        part = Student.objects.get(student_id=pk)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = StudentSerializer(part)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = StudentSerializer(part,data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        part.delete()
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

    # def post(self, request, *args, **kwargs):
    #     tutors_data = request.data.get("tutors", [])
        
    #     if not isinstance(tutors_data, list):
    #         return Response(
    #             {"detail": "Invalid data format. 'tutors' should be a list."},
    #             status=status.HTTP_400_BAD_REQUEST
    #         )
            
    #     serializer = TutorSerializer(data=tutors_data, many=True)
        
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
        
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RegistrationView(viewsets.ModelViewSet):
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer

# class DepartmentView(viewsets.ModelViewSet):
#     queryset = Department.objects.all()
#     serializer_class = DepartmentSerializer

class SemesterView(viewsets.ModelViewSet):
    queryset = Semester.objects.all()
    serializer_class = SemesterSerializer