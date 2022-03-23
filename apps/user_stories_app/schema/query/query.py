import graphene
from apps.user_stories_app.schema.mutation.user_story_mutation import Task, UserStory

from apps.user_stories_app.schema.type.type import TaskType, UserStoryType


class Query(graphene.AbstractType):
    user_stories = graphene.List(UserStoryType)
    Task = graphene.List(TaskType)
    user_story_by_id = graphene.Field(UserStoryType, id=graphene.Int(required=True))
    user_story_by_name = graphene.Field(UserStoryType, user_story_name=graphene.String(required=True))
    
    
    def resolve_user_stories(self, info):
        return UserStory.objects.all()
    
    def resolve_task(self, info):
        return UserStory.objects.all()
    
    def resolve_project_by_id(self, info, id):
        if id is not None:
            return UserStory.objects.get(pk=id)
        return None
    
    def resolve_project_by_name(self, info, user_story_name):
        if user_story_name is not None:
            return UserStory.objects.get(user_story_name=user_story_name)
        return None
    