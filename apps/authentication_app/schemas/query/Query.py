import graphene
from apps.authentication_app.models import User
from apps.authentication_app.schemas.type.type import UserType


class Query(graphene.AbstractType):
    # me = graphene.Field(UserType)
    users = graphene.List(UserType)

    def resolve_users(self, info):
        return User.objects.all()

    # def resolve_me(self, info):
    #     user = info.context.user
    #     if user.is_anonymous:
    #         raise Exception('Not logged in!')

    #     return user
    