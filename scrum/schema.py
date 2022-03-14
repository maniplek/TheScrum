import graphene

from apps.projectManagementApp.schema.query.query import Query as ProjectManagementQueries
from apps.projectManagementApp.schema.mutation.mutation import Mutation as ProjectMutation


class Query(graphene.ObjectType, ProjectManagementQueries):
    pass

class Mutation(ProjectMutation):
    pass

schema = graphene.Schema(query=Query,mutation=Mutation)
