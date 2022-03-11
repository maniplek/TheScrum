from graphene import ObjectType
import graphene
from apps.projectManagementApp.models import Project

from apps.projectManagementApp.schema.type import ProjectType


class Query(graphene.AbstractType):
    project = graphene.Field(ProjectType, id=graphene.Int())

    def resolve_project(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Project.objects.get(pk=id)

        return None
