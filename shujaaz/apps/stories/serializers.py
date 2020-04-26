from rest_framework import serializers
from .models import Stories


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
