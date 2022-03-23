from graphene_django import DjangoObjectType

from apps.user_stories_app.models import CreateUserStory


class UserStoryType(DjangoObjectType):
    class Meta:
        model = CreateUserStory
        field = ("__all__")
        