import graphene
import graphql_jwt
from apps.authentication_app.schemas.mutation.user_mutation import ChangePassword, CreateUser, IsVerified, RefreshOtp, RequestChangPassword
# from graphql_auth import mutations
from graphql_auth.schema import UserQuery, MeQuery

class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()
    is_verified = IsVerified.Field()
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    refresh_otp = RefreshOtp.Field()
    Verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()
    request_change_password = RequestChangPassword.Field()
    change_password =ChangePassword.Field()
    