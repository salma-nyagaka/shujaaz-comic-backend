from rest_framework import serializers
from .models import Stories, Characters


class StoriesSerializer(serializers.ModelSerializer):

    """
    Class for serializing the stories data.
    """


    class Meta:

        """
        Class to return all the fields data.
        """

        model = Stories
        fields = '__all__'


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
