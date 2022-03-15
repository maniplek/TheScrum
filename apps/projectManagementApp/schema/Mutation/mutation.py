import graphene

from apps.projectManagementApp.schema.mutation.create_project_mutation import CreateProject, UpdateProject


class Mutation(graphene.ObjectType):
    create_project = CreateProject.Field()
    update_project=UpdateProject.Field()
