import graphene

from apps.project_management.schema.mutation.project_mutation import CreateProject, UpdateProject


class Mutation(graphene.ObjectType):
    create_project = CreateProject.Field()
    update_project=UpdateProject.Field()