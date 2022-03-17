from django.db import models

# Create your models here.
from django.db import models

from apps.authentication_app.models import User


class Project (models.Model):
    project_name = models.CharField(max_length=20)
    project_owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    

    def __str__(self):
        return self.name
