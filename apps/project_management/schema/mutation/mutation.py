import graphene

from apps.project_management.schema.mutation.project_mutation import AcceptInvitation, InviteContributor, CreateProject, UpdateProject


class Mutation(graphene.ObjectType):
    create_project = CreateProject.Field()
    update_project = UpdateProject.Field()
    invite_contributor = InviteContributor.Field()
    accept_invitation=AcceptInvitation.Field()
