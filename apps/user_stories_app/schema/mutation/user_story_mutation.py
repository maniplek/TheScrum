import graphene
from apps.project_management.models import Project
from apps.user_stories_app.models import Task, UserStory
from graphql_jwt.decorators import login_required
from apps.user_stories_app.schema.type.type import SprintType, TaskLabelType, TaskStatusType, TaskType, UserStoryType


class CreateUserStory(graphene.Mutation):
    class Arguments:
        user_story_name = graphene.String(required=True)
        user_story_description = graphene.String(required=True)
        project_id = graphene.ID(required=True)

    user_story = graphene.Field(UserStoryType)

    @login_required
    def mutate(self, info, project_id, user_story_name, user_story_description):
        user = info.context.user
        if user.is_anonymous:
            raise Exception('You must be logged in!')

        project_instance = Project.objects.get(pk=project_id)
        if project_instance == None:
            raise Exception(f'Project with id {project_id} does not exist')

        if not project_instance.project_owner == user:
            raise Exception(f"You don't own project with id {project_id} ")

        user_story = UserStory()
        user_story.user_story_name = user_story_name
        user_story.user_story_description = user_story_description
        user_story.project = project_instance
        user_story.save()

        return CreateUserStory(user_story=user_story)


class UpdateUserStory(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
        user_story_name = graphene.String(required=True)
        user_story_description = graphene.String(required=True)

    user_story = graphene.Field(UserStoryType)

    def mutate(cls, root, info, id, **kwargs):
        user_story = UserStory.objects.get(pk=id)

        if user_story:
            user_story.user_story_name = kwargs.get('user_story_name')
            user_story.user_story_description = kwargs.get(
                'user_story_description')
            user_story.save()
            return UpdateUserStory(user_story=user_story)

        return UpdateUserStory(user_story=None)


class DeleteUserStory(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
        user_story_name = graphene.String(required=True)
        user_story_description = graphene.String(required=True)

    user_story = graphene.Field(UserStoryType)

    def mutate(cls, root, info, id, **kwargs):
        user_story = UserStory.objects.get(pk=id)

        if user_story:
            user_story.delete()
            return DeleteUserStory(message='User Story Successfuly Deleted ')

        return DeleteUserStory(user_story=None)


# task mutation
class CreateTaskMutation(graphene.Mutation):
    class Arguments:
        task_name = graphene.String(required=True)
        task_description = graphene.String(required=True)
        duration = graphene.String(required=True)
        task_label = graphene.String(required=True)
        is_blocked_by = graphene.String(required=True)

    task = graphene.Field(TaskType)

    def mutate(self, root, *args, **kwargs):
        task = Task()
        task.task_name = kwargs.get('task_name')
        task.task_description = kwargs.get('task_description')
        task.duration = kwargs.get('duration')
        task.task_label = kwargs.get('task_label')
        task.is_blocked_by = kwargs.get('is_blocked_by')
        task.save()

        return CreateTaskMutation(task=task)

    # sprint mutation


class CreateSprintMutation(graphene.Mutation):
    class Arguments:
        sprint_name = graphene.String(required=True)
        sprint_start_date = graphene.DateTime()
        sprint_end_date = graphene.DateTime()

    sprint = graphene.Field(SprintType)

    def mutate(self, root, *args, **kwargs):
        sprint = UserStory()
        sprint.sprint_name = kwargs.get('sprint_name')
        sprint.sprint_start_date = kwargs.get('sprint_start_date')
        sprint.sprint_end_date = kwargs.get('sprint_end_date')
        sprint.save()

        return CreateSprintMutation(sprint=sprint)

# task_label mutation


class CreateTaskLabel(graphene.Mutation):
    class Arguments:
        task_label_name = graphene.String(required=True)

    task_label = graphene.Field(TaskLabelType)

    @classmethod
    def mutate(self, root, *args, **kwargs):
        task_label = UserStory()
        task_label.task_label_name = kwargs.get('task_label_name')
        task_label.save()

        return CreateTaskLabel(task_label=task_label)

# task_Status mutation


class CreateTaskStatus(graphene.Mutation):
    class Arguments:
        task_status_name = graphene.String(required=True)

    task_status = graphene.Field(TaskStatusType)

    @classmethod
    def mutate(self, root, *args, **kwargs):
        task_status = UserStory()
        task_status.task_status_name = kwargs.get('task_status_name')
        task_status.save()

        return CreateTaskStatus(task_status=task_status)
