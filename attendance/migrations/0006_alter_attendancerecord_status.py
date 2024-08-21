# Generated by Django 5.1 on 2024-08-21 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0005_attendancerecord_is_absent_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendancerecord',
            name='status',
            field=models.CharField(choices=[('Present', 'Present'), ('Absent', 'Absent'), ('Late', 'Late'), ('Half-day', 'Half-day')], default='Absent', max_length=10),
        ),
    ]
