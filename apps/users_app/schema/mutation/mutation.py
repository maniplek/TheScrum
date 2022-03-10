from venv import create
import graphene 

from apps.users_app.schema.mutation.create_user_mutation import CreateUser

class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()