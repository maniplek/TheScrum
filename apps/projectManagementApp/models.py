from django.db import models


class Project (models.Model):
    project_name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

