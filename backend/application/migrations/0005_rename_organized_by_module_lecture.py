# Generated by Django 3.2.20 on 2023-08-01 16:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0004_module_organized_by'),
    ]

    operations = [
        migrations.RenameField(
            model_name='module',
            old_name='organized_by',
            new_name='Lecture',
        ),
    ]