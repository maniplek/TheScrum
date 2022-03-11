import graphene

from apps.projectManagementApp.schema.query.query import CreateProject


class Mutation(graphene.ObjectType):
    create_project=CreateProject.Field()
    