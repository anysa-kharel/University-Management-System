# Generated by Django 3.2.20 on 2023-08-05 08:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lecturer',
            fields=[
                ('id', models.IntegerField(unique=True)),
                ('lecturer_number', models.CharField(max_length=10, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('room_number', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Module',
            fields=[
                ('module_id', models.IntegerField(unique=True)),
                ('module_code', models.CharField(max_length=20, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('lecturer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='application.lecturer')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('student_id', models.IntegerField(unique=True)),
                ('student_number', models.CharField(max_length=20, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Tutor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lecturer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='application.lecturer')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='application.student')),
            ],
        ),
        migrations.CreateModel(
            name='Semester',
            fields=[
                ('department_name', models.CharField(max_length=50)),
                ('sem', models.IntegerField(primary_key=True, serialize=False)),
                ('module_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Semester_Module', to='application.module')),
            ],
        ),
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('registration_id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('registration_date', models.DateField(auto_now=True)),
                ('module', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='application.module')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='application.student')),
            ],
        ),
        migrations.CreateModel(
            name='Lecture',
            fields=[
                ('lecture_id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('time', models.CharField(max_length=10)),
                ('room', models.CharField(max_length=10)),
                ('day', models.CharField(max_length=10)),
                ('lecturer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='application.lecturer')),
                ('module_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='application.module')),
            ],
        ),
    ]
