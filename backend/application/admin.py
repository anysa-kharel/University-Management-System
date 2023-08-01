from django.contrib import admin
from .models import Lecturer
# Register your models here.

class LecturerAdmin(admin.ModelAdmin):
    list = ('lecture_number','name','room_number')

admin.site.register(Lecturer, LecturerAdmin)