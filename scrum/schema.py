import graphene

from apps.project_management.schema.query.query import Query as ProjectManagementQueries
from apps.project_management.schema.mutation.mutation import Mutation as ProjectMutation
from apps.authentication_app.schemas.query.Query import Query as UserQueries
from apps.user_stories_app.schema.query.query import Query as UserStoryQueries
from apps.authentication_app.schemas.mutation.mutation import Mutation as UserMutation
from apps.user_stories_app.schema.mutation.mutation import Mutation as CreateUserStoryMutation



class Query(graphene.ObjectType, ProjectManagementQueries,UserQueries, UserStoryQueries):
    pass


class Mutation(ProjectMutation, CreateUserStoryMutation,  UserMutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
