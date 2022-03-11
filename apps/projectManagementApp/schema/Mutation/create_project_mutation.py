import graphene

from apps.projectManagementApp.models import Project
from apps.projectManagementApp.schema.type import ProjectType


class CreateProject(graphene.Mutation):
    class Arguments:
        projectName = graphene.String(required=True)
        
    project = graphene.Field(ProjectType)

    def mutate(cls, name):
        project = Project
        project.project_name = name
        project.save()
        
        return CreateProject(project=project)