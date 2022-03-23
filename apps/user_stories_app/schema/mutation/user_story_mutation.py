from email import message
from msilib.schema import Class
from typing_extensions import Required
import graphene
from apps.user_stories_app.models import CreateUserStory

from apps.user_stories_app.schema.type.type import UserStoryType


class UserStory(graphene.Mutation):
    class Arguments:
        user_story_name = graphene.String(required=True) 
        user_story_description = graphene.String(required=True)
        # project_id = graphene.String(required=True)
    
    user_story = graphene.Field(UserStoryType)
      
    @classmethod
    def mutate(self, root, *args, **kwargs):
        user_story = CreateUserStory()
        user_story.user_story_name = kwargs.get('user_story_name')
        user_story.user_story_description = kwargs.get('user_story_description')
        user_story.save()
        
        return UserStory(user_story=user_story)
    
class UpdateUserStory(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
        user_story_name = graphene.String(required=True)
        user_story_description = graphene.String(required=True)
            
    user_story = graphene.Field(UserStoryType)
        
    @classmethod
    def mutate(cls, root, info, id, **kwargs):
        user_story = UserStory.objects.get(pk=id)
            
        if user_story:
            user_story.user_story_name = kwargs.get('user_story_name')
            user_story.user_story_description = kwargs.get('user_story_description')
            user_story.save()
            return UpdateUserStory(user_story = user_story)
            
        return UpdateUserStory(user_story=None)   
    
class DeleteUserStory(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
        user_story_name = graphene.String(required=True)
        user_story_description = graphene.String(required=True)
            
    user_story = graphene.Field(UserStoryType)
        
    @classmethod
    def mutate(cls, root, info, id, **kwargs):
        user_story = UserStory.objects.get(pk=id)
            
        if user_story:
            user_story.delete()
            return DeleteUserStory(message='User Story Successfuly Deleted ')
            
        return DeleteUserStory(user_story=None) 
                