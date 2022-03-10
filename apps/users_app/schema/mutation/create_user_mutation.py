# from typing_extensions import Required
import graphene 

from apps.users_app.models import CustomUser
from apps.users_app.schema.type.type import UserType

class CreateUser(graphene.Mutation):
    class Arguments:
        first_name = graphene.String(required=True)
        last_name =  graphene.String(required=True)
        email = graphene.String(required=True)
    
    user = graphene.Field(UserType)
    
    @classmethod
    def mutate(cls, root, info, first_name, last_name, email):
        user = CustomUser()
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.save()
        