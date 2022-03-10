import graphene

from apps.projectManagementApp.schema.Mutation.project_mutation import CreateProject


class Mutation(graphene.ObjectType):
    create_project = CreateProject.Field()