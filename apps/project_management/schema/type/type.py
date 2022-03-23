import graphene
from graphene_django import DjangoObjectType

from apps.project_management.models import Project

class ProjectInput(graphene.InputObjectType):
    id = graphene.ID()
    project_name = graphene.String()

class ProjectType(DjangoObjectType):
    class Meta:
        model = Project
        fields = ("__all__")   
