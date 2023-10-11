# Generated by Django 4.2.6 on 2023-10-11 05:57

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dataDrive', '0004_alter_file_employee_alter_folder_employee'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Employee',
            new_name='CustomUser',
        ),
        migrations.RenameField(
            model_name='file',
            old_name='employee',
            new_name='custom_user',
        ),
        migrations.RenameField(
            model_name='folder',
            old_name='employee',
            new_name='custom_user',
        ),
    ]
