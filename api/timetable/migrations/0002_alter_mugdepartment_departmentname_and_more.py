# Generated by Django 4.2.4 on 2023-09-10 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mugdepartment',
            name='departmentName',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='timetable',
            name='name',
            field=models.CharField(max_length=45),
        ),
    ]
