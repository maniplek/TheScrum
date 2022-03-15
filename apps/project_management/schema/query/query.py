from graphene import ObjectType
import graphene
from apps.project_management.models import Project

from apps.project_management.schema.type.type import ProjectType


class Query(graphene.AbstractType):
    project_by_id = graphene.Field(ProjectType, id=graphene.Int(required=True))
    project_by_name = graphene.Field(
        ProjectType, name=graphene.String(required=True))
    projects = graphene.List(ProjectType)

    def resolve_project_by_id(self, info, id):
        if id is not None:
            return Project.objects.get(pk=id)
        return None

    def resolve_project_by_name(self, info, name):
        if name is not None:
            return Project.objects.get(project_name=name)
        return None

    def resolve_projects(self, info, **kwargs):
        return Project.objects.all()