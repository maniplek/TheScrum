import graphene

from apps.projectManagement.models import Project
from apps.projectManagement.schema.type.type import ProjectType


class CreateProject(graphene.Mutation):
    class Arguments:
        projectName = graphene.String(required=True)

    project = graphene.Field(ProjectType)

    @classmethod
    def mutate(self, root, *args, **kwargs):
        project = Project()
        project.project_name = kwargs.get('projectName')
        project.save()

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
