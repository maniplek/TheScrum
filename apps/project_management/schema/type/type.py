import graphene
from graphene_django import DjangoObjectType

from apps.project_management.models import Project

class ProjectType(DjangoObjectType):
    class Meta:
        model = Project
        fields = ("id", "project_name")