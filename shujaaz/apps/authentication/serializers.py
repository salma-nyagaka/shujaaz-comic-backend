from django.contrib.auth import authenticate

from rest_framework import serializers, validators
from rest_framework.validators import UniqueValidator

from shujaaz.apps.authentication.backends import JWTAuthentication
from .models import User



class LoginSerializer(serializers.Serializer):
    """The class to serialize login details"""
    email = serializers.CharField(max_length=255)
    username = serializers.CharField(max_length=255, read_only=True)
    password = serializers.CharField(max_length=128, write_only=True)

    def validate(self, data):
        """
        The `validate` method is where we make sure that the current
        instance of `LoginSerializer` has "valid". In the case of logging a
        user in, this means validating that they've provided an email
        and password and that this combination matches one of the users in
        our database.
        """
        email = data.get('email', None)
        password = data.get('password', None)

        # As mentioned above, an email is required. Raise an exception if an
        # # email is not provided.
        # if email is None:
        #     raise serializers.ValidationError(
        #         'Your email address is required to log in.'
        #     )

        # As mentioned above, a password is required. Raise an exception if a
        # password is not provided.
        # if not password:
        #     raise serializers.ValidationError(
        #         'Kindly enter your password to log in.'
        #     )

        # The `authenticate` method is provided by Django and handles checking
        # for a user that matches this email/password combination. Notice how
        # we pass `email` as the `username` value. Remember that, in our User
        # model, we set `USERNAME_FIELD` as `username`.
        user = authenticate(email=email, password=password)

        # `authenticate` will return `None`. Raise an exception in this case.
        if user is None:
            raise serializers.ValidationError(
                'Either your email or password is not right. Double check '
                'them, or reset your password to log in. '
            )

        # Django provides a flag on our `User` model called `is_active`. The
        # purpose of this flag to tell us whether the user has been banned
        # or otherwise deactivated. This will almost never be the case, but
        # it is worth checking for. Raise an exception in this case.
        # if not user.is_active:
        #     raise serializers.ValidationError(
        #         'Your account is inactive. Kindly check your email for an '
        #         'activation link to activate '
        #     )
        token = JWTAuthentication.generate_token(email)

        """
        The `validate` method should return a dictionary of validated data.
        This is the data that is passed to the `create` and `update` methods
        that we will see later on.
        """
        return {
            'email': user.email,
            'username': user.username,
            'token': token
        }