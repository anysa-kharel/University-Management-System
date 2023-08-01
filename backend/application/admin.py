from django.contrib import admin
from .models import Lecturer, Student
# Register your models here.

class LecturerAdmin(admin.ModelAdmin):
    list = ('lecture_number','name','room_number')

admin.site.register(Lecturer, LecturerAdmin)


class StudentAdmin(admin.ModelAdmin):
    list = ('student_number','name')

admin.site.register(Student, StudentAdmin)
