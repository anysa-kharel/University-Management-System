from django.contrib import admin
from .models import *
# Register your models here.

class LecturerAdmin(admin.ModelAdmin):
    list = ('lecture_number','name','room_number')

admin.site.register(Lecturer, LecturerAdmin)


class StudentAdmin(admin.ModelAdmin):
    list = ('student_number','name')

admin.site.register(Student, StudentAdmin)

class ModuleAdmin(admin.ModelAdmin):
    list = ('module_code', 'name', 'organized_by')

admin.site.register(Module,ModuleAdmin)

class LectureAdmin(admin.ModelAdmin):
    list = ('lecture_id', 'room', 'delivered_by')

admin.site.register(Lecture, LectureAdmin)


class TutorAdmin(admin.ModelAdmin):
    list = ('lecturer_number','student_number')

admin.site.register(Tutor, TutorAdmin)

class RegistrationAdmin(admin.ModelAdmin):
    list = ('registration_id','student','module','registration_date')

admin.site.register(Registration, RegistrationAdmin)