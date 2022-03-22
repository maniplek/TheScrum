from email import message
from operator import contains
from apps.authentication_app.models import User
import graphene
from graphql import GraphQLError
from apps.project_management.models import Contribution, Project, UserRole
from apps.project_management.schema.type.type import ProjectInput, ProjectType
from utils.send_email import SendMail


class CreateProject(graphene.Mutation):
    class Arguments:
        project_owner_id = graphene.ID(required=True)
        project_name = graphene.String(required=True)

    project = graphene.Field(ProjectType)

    @classmethod
    def mutate(self, root, info, project_name, project_owner_id):
        user = User.objects.get(pk=project_owner_id)

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
        project_name = graphene.String()
        project_contributor_id = graphene.ID()
        user_role = graphene.String()

    message = graphene.String()

    @classmethod
    def mutate(self, info, root, project_contributor_id, project_name, user_role):

        user_instance = User.objects.get(
            pk=project_contributor_id)

        project_instance = Project.objects.get(
            project_name=project_name)

        if user_instance == None:
            raise GraphQLError("Please register your email")

        if project_instance == None:
            raise GraphQLError("Project does not exist")

        user_role_exist = False

        for value in UserRole:
            if user_role == value.value:
                user_role_exist = True
            if user_role_exist:
                break
        if user_role_exist != True:
            raise GraphQLError("User role does not exist")

        if user_instance and project_instance:
            context = {
                "first_name": user_instance.first_name,
                "project_name": project_instance.project_name
            }
            email = SendMail(context=context,
                             to_email=[user_instance.email],
                             subject="Request for contribution",
                             template="email/invite_contributor.html")
            email.send()
            contribution=Contribution()
            contribution.user=user_instance
            contribution.project=project_instance
            contribution.user_role=user_role
            contribution.is_contributor=False
            contribution.save()
            
            return InviteContributor(message="Project invitation sent successfully")

class AcceptInvitation(graphene.Mutation):
    class Arguments:
        project_contributor_id = graphene.ID()
        contribution_id=graphene.ID()
        
    message = graphene.String()

    @classmethod
    def mutate(self, info, root, project_contributor_id, contribution_id):

        user_instance = User.objects.get(
            pk=project_contributor_id)

        contribution_instance=Contribution.objects.get(
            pk=contribution_id
        )
        
        if user_instance == None:
            raise GraphQLError("Please register your email")
        
        if contribution_instance.user != user_instance:
            raise GraphQLError("You have not been invited to contribute on this project")
        
        if contribution_instance==None:
            raise GraphQLError("Contribution does not exist")


        if user_instance and contribution_instance:
            contribution_instance.is_contributor=True
            contribution_instance.project.contributors.add(user_instance.id)
            contribution_instance.save()
            
            return AcceptInvitation(message="Project invitation accepted successfully")

class UpdateProject(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
        projectName = graphene.String(required=True)

    project = graphene.Field(ProjectType)

    @classmethod
    def mutate(cls, root, info, id, **kwargs):
        project = Project.objects.get(pk=id)

        if project:
            project.project_name = kwargs.get('projectName')
            project.save()
            return UpdateProject(project=project)

        return UpdateProject(project=None)
