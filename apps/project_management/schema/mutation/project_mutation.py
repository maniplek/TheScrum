from email import message
from operator import contains
from apps.authentication_app.models import User
import graphene
from graphql import GraphQLError
from apps.project_management.models import Contribution, Project, UserRole
from apps.project_management.schema.type.type import ProjectType
from utils.send_email import SendMail
from graphql_jwt.decorators import login_required


class CreateProject(graphene.Mutation):

    class Arguments:
        project_name = graphene.String(required=True)

    project = graphene.Field(ProjectType)

    @login_required
    def mutate(self, info, project_name):
        user = info.context.user

        if user.is_anonymous:
            raise Exception('You must be logged to create a project!')

        if user == None:
            raise GraphQLError("User does not exist")

        if not len(project_name) or project_name.isspace():
            raise GraphQLError(
                "A project should have a valid name with no whitespaces")

        project = Project()
        project.project_name = project_name
        project.project_owner = user
        project.save()
        return CreateProject(project=project)


class InviteContributor(graphene.Mutation):

    class Arguments:
        project_contributor_id = graphene.ID()
        project_name = graphene.String()
        user_role = graphene.String()

    message = graphene.String()

    @login_required
    def mutate(self, info, project_name, user_role, project_contributor_id):

        user_instance = info.context.user

        user = User.objects.get(pk=project_contributor_id)

        if user_instance.is_anonymous:
            raise Exception('You must be logged to create a project!')

        project_instance = Project.objects.get(
            project_name=project_name)

        if user == None:
            raise GraphQLError("User not registered")

        if project_instance == None:
            raise GraphQLError("Project does not exist")

        if project_instance.project_owner == user:
            user_role_exist = False
            for value in UserRole:
                if user_role == value.value:
                    user_role_exist = True
                if user_role_exist:
                    break
                if user_role_exist != True:
                    raise GraphQLError("User role does not exist")

        if user and project_instance:
            context = {
                "first_name": user.first_name,
                "project_name": project_instance.project_name
            }
            email = SendMail(context=context,
                             to_email=[user.email],
                             subject="Request for contribution",
                             template="email/invite_contributor.html")

            contribution = Contribution()
            contribution.user = user
            contribution.project = project_instance
            contribution.user_role = user_role
            contribution.is_contributor = False
            contribution.save()

            email.send()

            return InviteContributor(message="Project invitation sent successfully")


class AcceptInvitation(graphene.Mutation):
    class Arguments:
        contribution_id = graphene.ID()

    message = graphene.String()

    @login_required
    def mutate(self, info, contribution_id):

        user_instance = info.context.user
        if user_instance.is_anonymous:
            raise Exception('You must be logged to create a project!')

        contribution_instance = Contribution.objects.get(pk=contribution_id)

        if not contribution_instance.user==user_instance:
            raise Exception('You have not been invited to participate on this  project!')
            
        if user_instance and contribution_instance:
            contribution_instance.is_contributor = True
            contribution_instance.project.contributors.add(user_instance.id)
            contribution_instance.save()

            return AcceptInvitation(message="Project invitation accepted successfully")


class UpdateProject(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
        projectName = graphene.String(required=True)

    project = graphene.Field(ProjectType)

    @login_required
    def mutate(cls, root, info, id, **kwargs):

        user_instance = info.context.user

        if user_instance.is_anonymous:
            raise Exception('You must be logged to create a project!')

        project = Project.objects.get(pk=id)

        if project.owner != user_instance:
            raise Exception(
                'You must be the creator of this project to be make an edit!')

        if project:
            project.project_name = kwargs.get('projectName')
            project.save()
            return UpdateProject(project=project)

        return UpdateProject(project=None)
