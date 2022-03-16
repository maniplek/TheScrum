from turtle import update
import graphene
from graphql_jwt import Verify

from apps.project_management.schema.query.query import Query as ProjectManagementQueries
from apps.project_management.schema.mutation.mutation import Mutation as ProjectMutation
from apps.authentication_app.schemas.query.Query import Query as UserQueries
from apps.authentication_app.schemas.mutation.mutation import Mutation as UserMutation


# class AuthMutation(graphene.ObjectType):

# , UserQuery
class Query(graphene.ObjectType, ProjectManagementQueries,UserQueries):
    pass


class Mutation(ProjectMutation,  UserMutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
