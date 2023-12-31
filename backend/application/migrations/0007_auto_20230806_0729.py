# Generated by Django 3.2.20 on 2023-08-06 07:29

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0006_rename_lecturer_id_lecturer_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='semester',
            name='department_name',
        ),
        migrations.RemoveField(
            model_name='semester',
            name='module_code',
        ),
        migrations.AddField(
            model_name='semester',
            name='module_code1',
            field=models.ForeignKey(default=django.utils.timezone.now, on_delete=django.db.models.deletion.CASCADE, related_name='Semester_Module1', to='application.module'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='semester',
            name='module_code2',
            field=models.ForeignKey(default=django.utils.timezone.now, on_delete=django.db.models.deletion.CASCADE, related_name='Semester_Module2', to='application.module'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='semester',
            name='module_code3',
            field=models.ForeignKey(default=django.utils.timezone.now, on_delete=django.db.models.deletion.CASCADE, related_name='Semester_Module3', to='application.module'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='semester',
            name='module_code4',
            field=models.ForeignKey(default=django.utils.timezone.now, on_delete=django.db.models.deletion.CASCADE, related_name='Semester_Module4', to='application.module'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='semester',
            name='module_code5',
            field=models.ForeignKey(default=django.utils.timezone.now, on_delete=django.db.models.deletion.CASCADE, related_name='Semester_Module5', to='application.module'),
            preserve_default=False,
        ),
    ]
