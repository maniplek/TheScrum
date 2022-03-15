from graphene import ObjectType
import graphene
from apps.project_management.models import Project

from apps.project_management.schema.type import ProjectType


class Query(graphene.AbstractType):
    project = graphene.Field(ProjectType, id=graphene.Int())

    def resolve_project(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Project.objects.get(pk=id)

        return None
