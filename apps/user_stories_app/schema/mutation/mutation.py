import graphene

from apps.user_stories_app.schema.mutation.user_story_mutation import DeleteUserStory, UpdateUserStory, UserStory


class Mutation(graphene.ObjectType):
    create_userStory = UserStory.Field()
    update_user_story = UpdateUserStory.Field()
    delete_user_story = DeleteUserStory.Field()