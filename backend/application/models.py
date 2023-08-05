from django.db import models

# Create your models here.

class Lecturer(models.Model):
    id = models.IntegerField(primary_key=True, unique=True )
    lecturer_number = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)
    room_number = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class Module(models.Model):
    module_code = models.CharField(max_length=10, primary_key=True,unique=True)
    name = models.CharField(max_length=100)
    lecturer = models.ForeignKey(Lecturer, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

class Semester(models.Model):
    sem = models.IntegerField(primary_key=True)
    module_code = models.ForeignKey(Module, on_delete=models.CASCADE)

    def __str__(self):
        return f"Semester: {self.sem}, Module: {self.module_code}"

class Lecture(models.Model):
    lecture_id = models.IntegerField(max_length=10, primary_key=True,unique=True) 
    time = models.CharField(max_length=10)
    room = models.CharField(max_length=10)
    date = models.DateField()
    lecturer_id = models.ForeignKey(Lecturer, on_delete=models.CASCADE)
    module_code = models.ForeignKey(Module, on_delete=models.CASCADE)

    def __str__(self):
        return f"Lecture ID: {self.lecture_id}, Time: {self.time}, Room: {self.room}"

class Student(models.Model):
    student_number = models.IntegerField(primary_key=True,unique=True)
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

# class LectureTutor(models.Model):
#     lecture = models.ForeignKey(Lecture, on_delete=models.CASCADE)
#     tutor = models.ForeignKey(Lecturer, on_delete=models.CASCADE)

#     def __str__(self):
#         return f"{self.lecture} - Tutor: {self.tutor}"

class Tutor(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    lecturer = models.ForeignKey(Lecturer, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.lecturer} - Student: {self.student}"

class Registration(models.Model):
    registration_id = models.IntegerField(primary_key=True,unique=True)
    registration_date = models.DateField(auto_now=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    module = models.ForeignKey(Module, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.student} - Module: {self.module} - Date: {self.registration_date}"