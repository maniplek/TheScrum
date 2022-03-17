from operator import contains
import re
from apps.authentication_app.models import User
import graphene
from graphql import GraphQLError
from apps.project_management.models import Project
from apps.project_management.schema.type.type import ProjectInput, ProjectType


class CreateProject(graphene.Mutation):

    class Arguments:
        projectName = graphene.String(required=True)
        projectOwnerId = graphene.ID()
    project = graphene.Field(ProjectType)

    @classmethod
    def mutate(self, root, info, projectName, projectOwnerId):
        user = User.objects.get(pk=projectOwnerId)

        if user == None:
           raise GraphQLError ("User does not exist")

        if not len(projectName) or not projectName.isspace():
            raise GraphQLError ("A project should have a valid name with no whitespaces")
        
        project = Project()
        project.project_name = projectName
        project.project_owner = user
        project.save()
        print()
        return CreateProject(project=project)


class UpdateProject(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
        projectName = graphene.String(required=True)

    project = graphene.Field(ProjectType)

    @classmethod
    def mutate(cls, root, info, id, **kwargs):
        project = Project.objects.get(pk=id)

        if project:
            project.project_name = kwargs.get('projectName')
            project.save()
            return UpdateProject(project=project)

        return UpdateProject(project=None)
