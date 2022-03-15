from cgitb import html
import graphene
from django.contrib.auth import get_user_model
from graphql import GraphQLError
from apps.authentication_app.models import User

from apps.authentication_app.schemas.type.type import UserType
from utils.send_email import SendMail


class CreateUser(graphene.Mutation):
    class Arguments:
        email = graphene.String(required=True)
        first_name = graphene.String()
        last_name = graphene.String()
        password=graphene.String(required=True)

    user = graphene.Field(UserType)

    @classmethod
    def mutate(self, root, *args, **kwargs):
        user:User =get_user_model().objects.create_user(
            email=kwargs.get("email"),
            password=kwargs.get("password"),
            first_name=kwargs.get("first_name"),
            last_name=kwargs.get("last_name"))
            
        
        if user:
            context = {
                "otp": user.OTP,
                "first_name": user.first_name
            }
            email = SendMail(context=context,
                             to_email=[user.email],
                             subject='scrum email verification',
                             temperate='email/activation_email.html')
            email.send()
            return CreateUser(user=user)
        
        else:
            raise GraphQLError("Something went wrong")
