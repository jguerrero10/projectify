from django.db import models
from django.contrib.auth.models import AbstractUser


class OperationalUser(AbstractUser):
    email = models.EmailField(unique=True)

    REQUIRED_FIELDS = [
        'password',
        'first_name',
        'last_name',
        'email'
    ]


class Project(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=180)


class Dedication(models.Model):
    user = models.ForeignKey(OperationalUser, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    date = models.DateField()
    isoweek = models.CharField(max_length=12, unique=True)
