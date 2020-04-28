from rest_framework import serializers
from .models import comic, Characters
from shujaaz.apps.user.serializers import UserSerializer


class ComicSerializer(serializers.ModelSerializer):

    """
    Class for serializing the user data.
    """

    creator =  UserSerializer()


    class Meta:

        """
        Class to return all the fields data.
        """

        model = comic
        fields = ('title', 'avatar', 'creator')



class CharacterSerializer(serializers.ModelSerializer):

    """
    Class for serializing the characters data.
    """


    class Meta:

        """
        Class to return all the fields data.
        """

        model = Characters
        fields = '__all__'
