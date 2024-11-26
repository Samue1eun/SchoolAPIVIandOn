# Generated by Django 5.1.3 on 2024-11-21 23:20

import student_app.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_app', '0006_student_subjects'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='good_student',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='locker_combination',
            field=models.CharField(default='12-12-12', max_length=255, validators=[student_app.validators.validate_combination_format]),
        ),
        migrations.AlterField(
            model_name='student',
            name='name',
            field=models.CharField(max_length=255, validators=[student_app.validators.validate_name_format]),
        ),
        migrations.AlterField(
            model_name='student',
            name='personal_email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
