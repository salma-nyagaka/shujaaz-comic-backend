import logging

from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin)
from django.db import models


# Get an instance of a logger
logger = logging.getLogger(__name__)

avatar = "https://res.cloudinary.com/mashafrancis/image/upload/v1552641620/kari4me/nan.jpg"


class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None, is_staff=False,
                    **extra_fields):
        """Create a user instance with the given email and password."""
        if username is None:
            raise TypeError('Users must have a username.')

        # Google OAuth2 backend send unnecessary username field
        extra_fields.pop("username", None)

        if email is None:
            raise TypeError('Users must have an email address.')

        email = self.normalize_email(email)

        user = self.model(username=username, email=email, **extra_fields)

        if password:
            user.set_password(password)
        user.save()

        return user


class User(AbstractBaseUser, PermissionsMixin):
    id = models.AutoField(primary_key=True)
    username = models.CharField(db_index=True, max_length=255, unique=True)
    email = models.EmailField(db_index=True, unique=True)
    first_name = models.CharField(max_length=256, blank=True)
    last_name = models.CharField(max_length=256, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # photo = models.CharField(blank=False, max_length=1024, default=avatar)

    # The `USERNAME_FIELD` property tells us which field we will use to log in.
    # In this case, we want that to be the username field.
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()


    @staticmethod
    def get_user(email):
        try:
            user = User.objects.get(email=email)
            return user

        except Exception:
            return False
