from rest_framework import serializers
from .models import *

class LecturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lecturer
        fields = ['lecturer_number', 'name', 'room_number']
