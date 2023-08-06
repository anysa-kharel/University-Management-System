from django.db import models

# Create your models here.

class Lecturer(models.Model):
    lecturer_number = models.CharField(max_length=10,primary_key=True ,unique=True)
    id = models.IntegerField( unique= True )
    name = models.CharField(max_length=100)
    room_number = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class Module(models.Model):
    module_code = models.CharField(max_length=20,primary_key=True,unique=True)
    module_id = models.IntegerField(unique=True)
    name = models.CharField(max_length=100)
    lecturer = models.ForeignKey(Lecturer, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name


# class Department(models.Model):
#     department_name = models.CharField(max_length=50,unique=True,primary_key=True)
#     def __str__(self):
#         return self.department_name

class Semester(models.Model):
    department_name = models.CharField(max_length=50)
    sem = models.IntegerField(primary_key=True)
    module_code = models.ForeignKey(Module, on_delete=models.CASCADE,related_name='Semester_Module')

    def __str__(self):
        return f"Semester: {self.sem},Department: {self.department_name}, Module: {self.module_code}"



class Lecture(models.Model):
    lecture_id = models.IntegerField(primary_key=True,unique=True) 
    time = models.CharField(max_length=10)
    room = models.CharField(max_length=10)
    day = models.CharField(max_length=10)
    lecturer_id = models.ForeignKey(Lecturer, on_delete=models.CASCADE)
    module_code = models.ForeignKey(Module, on_delete=models.CASCADE)

    def __str__(self):
        return f"Lecture ID: {self.lecture_id}, Time: {self.time}, Room: {self.room}"

class Student(models.Model):
    student_number = models.CharField(max_length=10,primary_key=True,unique=True)
    student_id = models.IntegerField( unique=True )
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
    tutor_id = models.IntegerField()

    def __str__(self):
        return f"{self.lecturer} - Student: {self.student}"

class Registration(models.Model):
    
    registration_id = models.IntegerField(primary_key=True,unique=True)
    registration_date = models.DateField(auto_now=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    module = models.ForeignKey(Module, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.student} - Module: {self.module} - Date: {self.registration_date}"