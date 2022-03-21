from django.db import models
from django.contrib.postgres.fields import ArrayField

from apps.authentication_app.models import User


class Project (models.Model):
    project_name = models.CharField(max_length=20, unique=True, null=False)
    project_owner = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True)
    contributors = models.ManyToManyField(
        User, related_name='project_contributors')

    def __str__(self):
        return self.project_name
