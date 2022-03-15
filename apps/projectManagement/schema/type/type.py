
from graphene_django import DjangoObjectType

from apps.projectManagement.models import Project


class ProjectType(DjangoObjectType):
    class Meta:
        model = Project
        fields = ("id", "project_name")

   