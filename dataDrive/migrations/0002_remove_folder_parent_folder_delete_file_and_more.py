# Generated by Django 4.2.6 on 2023-10-10 12:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dataDrive', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='folder',
            name='parent_folder',
        ),
        migrations.DeleteModel(
            name='File',
        ),
        migrations.DeleteModel(
            name='Folder',
        ),
    ]