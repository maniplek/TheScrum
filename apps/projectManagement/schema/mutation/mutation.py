import graphene

from apps.projectManagement.schema.mutation.mutation import CreateProject, UpdateProject


class Mutation(graphene.ObjectType):
    create_project = CreateProject.Field()
    update_project=UpdateProject.Field()
