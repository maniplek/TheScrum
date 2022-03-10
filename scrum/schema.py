import graphene

from apps.users_app.schema.query.query import Query as UserQuery
from apps.projectManagementApp.schema.query.query import Query as ProjectManagementQueries
from apps.projectManagementApp.schema.Mutation.mutation import Mutation as ProjectMutation
from apps.users_app.schema.mutation.mutation import Mutation as UserMutation
from graphql_auth import mutations
# from graphql_auth.schema import MeQuery

class AuthMutation(graphene.ObjectType):
   register = mutations.Register.Field()


class Query(graphene.ObjectType, ProjectManagementQueries, UserQuery):
    pass

class Mutation(ProjectMutation, AuthMutation, UserMutation, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query,mutation=Mutation)
