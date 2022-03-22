from datetime import datetime
import math
import random
from xmlrpc.client import Fault
from django.db import models
from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from utils.otp_generator_helper import otp_genator
from utils.validate_email import Validate_email as email_validation



  

class UserAccountManager(BaseUserManager,models.Manager):
    def _create_user(self, email, password, first_name, last_name, **extra_fields):
        if not email_validation.isvalidEmail(email):
            raise ValueError("invalid email")

        email = self.normalize_email(email)
        
        user = self.model(email=email,first_name=first_name,last_name=last_name,**extra_fields)
        user.OTP = otp_genator()
        user.set_password(password)
        user.save()
        return user

    def create_user(self, email, password, first_name, last_name, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        extra_fields.setdefault("is_active", True)
        return self._create_user(email, password,first_name,last_name, **extra_fields)

    def create_staff_user(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", False)
        extra_fields.setdefault("is_active", True)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)
        return self._create_user(email, password, **extra_fields)    


class User(AbstractBaseUser, PermissionsMixin):
   
    email = models.EmailField(_("Email address"), unique=True)
    is_verified = models.BooleanField(default=False, null=False)
    OTP =  models.IntegerField(unique=True)
    first_name = models.CharField(_("First name"), max_length=30, blank=True)
    last_name = models.CharField(_("Last name"), max_length=30, blank=True)
    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )
    is_active = models.BooleanField(
        _("active"),
        default=False,
        help_text=_("Designates whether this user should be treated as active."),
    )
    date_joined = models.DateTimeField(_("Date joined"), default=datetime.now())
    # format = '%Y/%m/%d %H:%M %p'
    otp_generated_time = models.DateTimeField(default=datetime.now())

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name"]
    
    objects=UserAccountManager()

    def __str__(self):
        return self.email

    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        full_name = "{} {}".format(self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        return self.first_name.strip()
