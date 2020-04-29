from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):

    """
    Class for serializing the user data.
    """

    class Meta:

        """
        Class to return all the fields data.
        """

        model = User
        fields = '__all__'
