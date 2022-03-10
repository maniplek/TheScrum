import graphene

from apps.projectManagementApp.models import Project
from apps.projectManagementApp.schema.type.type import ProjectType


class CreateProject(graphene.Mutation):
    class Arguments:
        projectName = graphene.String(required=True)
        
    project = graphene.Field(ProjectType)

    @classmethod
    def mutate(self, root,*args, **kwargs):
        project = Project()
        project.project_name = kwargs.get('projectName')
        project.save()
        
        return CreateProject(project=project)