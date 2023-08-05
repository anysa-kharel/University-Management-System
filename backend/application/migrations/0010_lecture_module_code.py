# Generated by Django 3.2.20 on 2023-08-05 02:59

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0009_alter_lecture_lecture_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='lecture',
            name='module_code',
            field=models.ForeignKey(default=django.utils.timezone.now, on_delete=django.db.models.deletion.CASCADE, to='application.module'),
            preserve_default=False,
        ),
    ]
