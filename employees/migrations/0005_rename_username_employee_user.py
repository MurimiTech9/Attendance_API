# Generated by Django 5.0.8 on 2024-08-13 12:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0004_rename_user_employee_username'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='username',
            new_name='user',
        ),
    ]
