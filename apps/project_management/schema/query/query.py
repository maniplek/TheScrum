import email
import graphene
from apps.project_management.models import Project

from apps.project_management.schema.type.type import ProjectType
from graphql_jwt.decorators import login_required


class Query(graphene.AbstractType):
    project_by_id = graphene.Field(ProjectType, id=graphene.Int(required=True))
    project_by_name = graphene.Field(
        ProjectType, name=graphene.String(required=True))
    projects = graphene.List(ProjectType)

    def resolve_project_by_name(self, info):

        user = info.context.user

        if user.is_anonymous:
            raise Exception('You must be logged to create a project!')

        if user:
            projects: Project = Project.objects.filter(project_owner=user)
            return projects.project_name

    @login_required
    def resolve_projects(self, info, **kwargs):

        user = info.context.user

        if user.is_anonymous:
            raise Exception('You must be logged to create a project!')

        if user:
            projects: Project = Project.objects.filter(project_owner=user)
            return projects
