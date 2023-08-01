from rest_framework import serializers
from .models import Lecturer,Student,Module

class LecturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lecturer
        fields = ('lecturer_number', 'name', 'room_number')

class ModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Module
        fields = '__all__'


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

