from cgitb import html
from datetime import datetime, timezone
from datetime import timedelta
# from django.utils import timezone
import email
from email import message
from email.policy import default
from pickle import NONE
import graphene
from django.contrib.auth import get_user_model
from graphql import GraphQLError
from setuptools import Require
from apps.authentication_app.models import User
from apps.authentication_app.schemas.type.type import UserType, VerifiedType
from utils.otp_generator_helper import otp_genator
from utils.send_email import SendMail


class CreateUser(graphene.Mutation):
    class Arguments:
        email = graphene.String(required=True)
        first_name = graphene.String()
        last_name = graphene.String()
        password = graphene.String(required=True)

    user = graphene.Field(UserType)

    @classmethod
    def mutate(self, root, *args, **kwargs):
        user: User = get_user_model().objects.create_user(
            email=kwargs.get("email"),
            password=kwargs.get("password"),
            first_name=kwargs.get("first_name"),
            last_name=kwargs.get("last_name"))

        if user:
            context = {
                "first_name": user.first_name,
                "message": f"Please use this OTP to activate your account: {user.OTP}\n"
                "This Otp will be Expired in 1min"
            }
            email = SendMail(context=context,
                             to_email=[user.email],
                             subject='scrum email verification',
                             template='email/activation_email.html')
            email.send()
            return CreateUser(user=user)

        else:
            raise GraphQLError("Something went wrong")


class IsVerified(graphene.Mutation):
    class Arguments:

        email = graphene.String(required=True)
        otp = graphene.Int(required=True)

    user = graphene.Field(VerifiedType)
    message = graphene.String()

    @classmethod
    def mutate(cls, root, info, **kwargs):
        input_email = kwargs.get('email')
        input_otp = kwargs.get('otp')

        new_now = datetime.now(timezone.utc) + timedelta(hours=4)
        user = get_user_model().objects.get(email=input_email)
        generated = (user.otp_generated_time) + timedelta(hours=2)
        diff = (new_now - generated).total_seconds()
        if not user:
            raise GraphQLError(
                f"user with {email} does not exist, Please SignUp ")
        elif user.is_verified:
            raise GraphQLError(f"user with {email} is aleady verified")
        elif not user.OTP == input_otp:
            raise GraphQLError("User can not be verified, wrong otp!")
        elif diff > 60000:
            raise GraphQLError(
                " OTP has been expired, Please send another refresh OTP ")
        else:
            user.is_verified = True
            user.save()
            return IsVerified(user=user, message=('user is verified successfuly'))


class RefreshOtp(graphene.Mutation):
    class Arguments:
        email = graphene.String(required=True)

    message = graphene.String()

    @classmethod
    def mutate(cls, root, info, email):
        user = User.objects.get(email=email)
        if not user:
            raise GraphQLError(
                f"user with {email} does not exist, Please SignUp ")
        elif user.is_verified:
            raise GraphQLError(f"user with {email} is aleady verified")
        else:
            user.OTP = otp_genator()
            user.otp_generated_time = timezone.now()
            user.save()
            context = {
                "otp": user.OTP,
                "first_name": user.first_name
            }
            email = SendMail(context=context,
                             to_email=[user.email],
                             subject='scrum email verification',
                             template='email/activation_email.html')
            email.send()
            return RefreshOtp(message='The new otp have been sent to your email')


class RequestChangePassword(graphene.Mutation):
    class Arguments:
        email = graphene.String(required=True)
    message = graphene.String()

    @classmethod
    def mutate(cls, root, info, email):
        user = None
        try:
            user: User = get_user_model().objects.get(email=email)
        except Exception as e:
            raise GraphQLError("Email not found, Please Register!")

        if user:
            user.OTP = otp_genator()
            user.otp_generated_time = datetime.now()
            user.save
            context = {
                "first_name": user.first_name,
                "message": f"Reset your password using this otp: {user.OTP}\n"
                "This Otp will be Expired in 1min"
            }
            email = SendMail(context=context,
                             to_email=[user.email],
                             subject='scrum change password',
                             template='email/activation_email.html')
            email.send()

            return RequestChangePassword(message="Please check your email for changing the password")


class ChangePassword(graphene.Mutation):
    class Arguments:
        email = graphene.String()
        otp = graphene.Int()
        password = graphene.String()

    message = graphene.String()

    @classmethod
    def mutate(cls, root, info, email, otp, password):
        user = None
        try:
            user: User = get_user_model().objects.get(email=email)
        except Exception as e:
            raise GraphQLError("Email not found, Please Register!")
        if user:
            new_now = datetime.now(timezone.utc) + timedelta(hours=4)
            generated = (user.otp_generated_time) + timedelta(hours=2)
            diff = (new_now - generated).total_seconds()
            if not user.OTP == otp:
                raise GraphQLError("Please Request change password!")
            elif diff > 60000:
                raise GraphQLError(
                    " OTP has been expired, Please send another refresh OTP ")
            else:
                user.set_password(password)
                user.save()
                return ChangePassword(message="Password successfuly changed.")
        else:
            raise GraphQLError("Email not found, Please Register!")
