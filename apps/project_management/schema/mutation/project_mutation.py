from email import message
from operator import contains
from apps.authentication_app.models import User
import graphene
from graphql import GraphQLError
from apps.project_management.models import Project
from apps.project_management.schema.type.type import ProjectInput, ProjectType
from utils.send_email import SendMail


class CreateProject(graphene.Mutation):

    class Arguments:
        projectName = graphene.String(required=True)
        projectOwnerId = graphene.ID()
    project = graphene.Field(ProjectType)

    @classmethod
    def mutate(self, root, info, projectName, projectOwnerId):
        user = User.objects.get(pk=projectOwnerId)

        if user == None:
            raise GraphQLError("User does not exist")

        if not len(projectName) or projectName.isspace():
            raise GraphQLError(
                "A project should have a valid name with no whitespaces")

        project = Project()
        project.project_name = projectName
        project.project_owner = user
        project.save()
        return CreateProject(project=project)


class RequestContributor(graphene.Mutation):

    class Arguments:
        project_name = graphene.String()
        project_contributor_id = graphene.ID()

    project = graphene.Field(ProjectType)
    message = graphene.String()

    @classmethod
    def mutate(self, info, root, project_contributor_id, project_name):
        print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
        user_instance = User.objects.get(
            pk=project_contributor_id)
        print(f'>>>>>>>>>>>>>>>>>{user_instance.email}')
        project_instance = Project.objects.get(
            project_name=project_name)
        print(f'>>>>>>>>>>>>>>>>>{project_instance.project_name}')

        if user_instance == None:
            raise GraphQLError("Please register your email")

        # if user.is_verified == False:
        #     raise GraphQLError("Your account needs to be verified")

        # check graphql user is logged-in
        if project_instance == None:
            raise GraphQLError("Project does not exist")

        if user_instance and project_instance:
            context = {
                "first_name": user_instance.first_name,
                "project_name": project_instance.project_name
            }
            email = SendMail(context=context,
                             to_email=[user_instance.email],
                             subject="Request for contribution",
                             template="templates/email/invite_contributor.html")
            email.send()
            return RequestContributor(message="Project invitation sent successfully")
        # project_instance.contributors.add(user_instance.id)
        # project_instance.save()
        # return RequestContributor(project=project_instance)


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
