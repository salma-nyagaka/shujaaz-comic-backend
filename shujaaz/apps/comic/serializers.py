from rest_framework import serializers
from .models import Comic, Characters
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

        model = Comic
        fields = ('title', 'avatar', 'summary', 'creator')



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
