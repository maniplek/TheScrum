from enum import Enum
from django.db import models

from apps.authentication_app.models import User


class Project (models.Model):
    project_name = models.CharField(max_length=20, unique=True, null=False)
    project_owner = models.ForeignKey(
        User, on_delete=models.CASCADE)
    contributors = models.ManyToManyField(
        User, through='Contribution', related_name="contributors")

    def __str__(self):
        return self.project_name


class UserRole(Enum):
    PO = "Project_owner"
    SM = "Scrum_master"
    DE = "Developer"

    @classmethod
    def choices(cls):
        return[(key.value, key.name) for key in cls]


class Contribution(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE)
    user_role = models.CharField(max_length=20, choices=UserRole.choices())
    is_contributor = models.BooleanField(default=False)
