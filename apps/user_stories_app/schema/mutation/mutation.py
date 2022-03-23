import graphene

from apps.user_stories_app.schema.mutation.user_story_mutation import  CreateSprintMutation, CreateTaskLabel, CreateTaskMutation, CreateTaskStatus, DeleteUserStory,   UpdateUserStory, CreateUserStory


class Mutation(graphene.ObjectType):
    create_userStory = CreateUserStory.Field()
    update_user_story = UpdateUserStory.Field()
    delete_user_story = DeleteUserStory.Field()
    create_task = CreateTaskMutation.Field()
    task_sprint =  CreateSprintMutation.Field() 
    create_task_label = CreateTaskLabel.Field() 
    create_task_status = CreateTaskStatus.Field()