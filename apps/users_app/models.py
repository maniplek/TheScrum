from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class CustomUser(AbstractUser):
    
    first_name = models.CharField(max_length=45, unique=False)
    last_name = models.CharField(max_length=45, unique=False)
    email = models.EmailField(blank=False, max_length=255, verbose_name="email address",  unique = True)
    # user_story = models.ForeignKey(UserStory, on_delete=models.CASCADE)      
    
    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
    def __str__(self):
        return "{}".format(self.email)