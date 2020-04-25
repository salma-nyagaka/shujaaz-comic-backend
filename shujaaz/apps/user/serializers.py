from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):

    """
    Class for serializing the user data.
    """

    id = serializers.CharField(required=False)
    username = serializers.CharField(required=False)
    first_name = serializers.DateTimeField(required=False)
    last_name = serializers.CharField(required=False)
    email = serializers.CharField(required=False)

    class Meta:

        """
        Class to return all the fields.
        """

        model = User
        fields = '__all__'

