# Generated by Django 4.2.6 on 2023-10-11 07:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dataDrive', '0005_rename_employee_customuser_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='file',
            name='name',
        ),
    ]