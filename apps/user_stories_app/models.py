from pyexpat import model
from django.db import models
from django.db.models.deletion import CASCADE

from apps.project_management.models import Project

# Create your models here.

class CreateUserStory(models.Model):
    user_story_name = models.CharField(max_length=255)
    user_story_description = models.CharField(max_length=255)
    project_id = models.ForeignKey(Project, on_delete=CASCADE )
    
    def __str__(self):
        return self.user_story_name
        