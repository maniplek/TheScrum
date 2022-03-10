from dataclasses import field
from pyexpat import model
from graphene_django import DjangoObjectType
from apps.users_app.models import CustomUser


class UserType(DjangoObjectType):
    class Meta:
        model = CustomUser
        fields = ("first_name","last_name","email")