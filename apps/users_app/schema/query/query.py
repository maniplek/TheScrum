from graphene import ObjectType
import graphene
from apps.users_app.models import CustomUser
from apps.users_app.schema.type.type import UserType

class Query(graphene.AbstractType):
    user = graphene.Field(UserType, id=graphene.Int())
    
    def resolve_user(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return CustomUser.objects.get(pk=id) 

        return None
        