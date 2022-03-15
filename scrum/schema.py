import graphene

from apps.projectManagement.schema.query.query import Query as ProjectManagementQueries
from apps.projectManagement.schema.mutation.mutation import Mutation as ProjectMutation


class Query(graphene.ObjectType, ProjectManagementQueries):
    pass

class Mutation(ProjectMutation):
    pass

schema = graphene.Schema(query=Query,mutation=Mutation)
