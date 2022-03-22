from dataclasses import fields
from pyexpat import model
from graphene_django import DjangoObjectType

from apps.authentication_app.models import User


class UserType(DjangoObjectType):
    
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email')


class VerifiedType(DjangoObjectType):
    class Meta:
        model = User
        fields = ("otp", "email") 

class RefreshOtpType(DjangoObjectType):
    class Meta:
        model = User
        fields = ()
    