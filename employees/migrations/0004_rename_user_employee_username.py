# Generated by Django 5.0.8 on 2024-08-13 12:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0003_alter_employee_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='user',
            new_name='username',
        ),
    ]
