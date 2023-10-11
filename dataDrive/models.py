from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class CustomUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=10)


class Folder(models.Model):
    custom_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, default="untitled Folder")
    parent_folder = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)


class File(models.Model):
    custom_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    parent_folder = models.ForeignKey(Folder, null=True, blank=True, on_delete=models.CASCADE)
    file = models.FileField(upload_to='uploads/', default=False)
