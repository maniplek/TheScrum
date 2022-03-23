from datetime import datetime
from enum import Enum
from django.db import models
from django.db.models.deletion import CASCADE

from apps.project_management.models import Project


class UserStory(models.Model):
    user_story_name = models.CharField(max_length=255)
    user_story_description = models.CharField(max_length=255)
    project = models.ForeignKey(Project, on_delete=CASCADE)

    def __str__(self):
        return self.user_story_name

    # sprint Fields


class TaskSprint(models.Model):
    sprint_name = models.CharField(max_length=255)
    sprint_start_date = models.DateTimeField(default=datetime.now())
    sprint_end_date = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return self.sprint_name

    # task label fields


class TaskLabel(models.Model):
    task_label_name = models.CharField(max_length=255)
    # task_id = models.ForeignKey(UserStory, on_delete=CASCADE )

    def __str__(self):
        return self.task_label_name

    # task status field


class TaskStatus(models.Model):
    task_status_name = models.CharField(max_length=255)

    def __str__(self):
        return self.task_status_name


class Priority(Enum):
    H = "HIGH"
    M = "MODERATE"
    L = "LOW"

    @classmethod
    def choices(cls):
        return[(key.value, key.name) for key in cls]

   # task fields


class Task(models.Model):
    task_name = models.CharField(max_length=255)
    task_description = models.CharField(max_length=255)
    duration = models.CharField(max_length=255)
    task_label = models.CharField(max_length=255)
    is_blocked_by = models.CharField(max_length=255)
    user_story = models.ForeignKey(UserStory, on_delete=CASCADE)
    sprint = models.ForeignKey(TaskSprint, on_delete=CASCADE)
    task_label = models.ForeignKey(TaskLabel, on_delete=CASCADE)
    task_status = models.ForeignKey(TaskStatus, on_delete=CASCADE)

    def __str__(self):
        return self.task_name
