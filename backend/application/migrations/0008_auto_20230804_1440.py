# Generated by Django 3.2.20 on 2023-08-04 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0007_delete_lecturetutor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='registration_date',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='registration',
            name='registration_id',
            field=models.CharField(max_length=10, primary_key=True, serialize=False),
        ),
    ]
