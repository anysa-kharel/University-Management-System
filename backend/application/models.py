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
    sem = models.IntegerField(primary_key=True)
    faculty = models.CharField(max_length=30)
    module_code1 = models.ForeignKey(Module ,related_name='Semester_Module1', on_delete=models.CASCADE)
    module_code2 = models.ForeignKey(Module ,related_name='Semester_Module2', on_delete=models.CASCADE)
    module_code3 = models.ForeignKey(Module ,related_name='Semester_Module3', on_delete=models.CASCADE)
    module_code4 = models.ForeignKey(Module ,related_name='Semester_Module4', on_delete=models.CASCADE)
    module_code5 = models.ForeignKey(Module ,related_name='Semester_Module5', on_delete=models.CASCADE)
    
# address1 = models.ForeignKey(Address, verbose_name=_("Address1"),related_name="Address1", null=True, blank=True,on_delete=models.SET_NULL)

# address2 = models.ForeignKey(Address, verbose_name=_("Address2"),related_name="Address2", null=True, blank=True,on_delete=models.SET_NULL)

    def __str__(self):
        return f"Semester: {self.sem}"



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