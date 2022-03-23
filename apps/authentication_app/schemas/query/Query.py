import graphene
from apps.authentication_app.models import User
from graphql_jwt.decorators import login_required
from apps.authentication_app.schemas.type.type import UserType


class Query(graphene.AbstractType):
    me = graphene.Field(UserType)
    users = graphene.List(UserType)
    

    def resolve_users(self, info):
        return User.objects.all()
      

    def resolve_viewer(self, info, **kwargs):
        user = info.context.user
        if not user.is_authenticated:
            raise Exception("Authentication credentials were not provided")
        return user
   