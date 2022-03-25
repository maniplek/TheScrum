from graphene_django import DjangoObjectType

from apps.user_stories_app.models import Task, TaskLabel, TaskSprint, TaskStatus, UserStory


class UserStoryType(DjangoObjectType):
    class Meta:
        model = UserStory
        field = ("__all__")


class TaskType(DjangoObjectType):
    class Meta:
        model = Task
        field = ("__all__")


class SprintType(DjangoObjectType):
    class Meta:
        model = TaskSprint
        field = ("__all__")


class TaskLabelType(DjangoObjectType):
    class Meta:
        model = TaskLabel
        field = ("__all__")


class TaskStatusType(DjangoObjectType):
    class Meta:
        model = TaskStatus
        field = ("__all__")
