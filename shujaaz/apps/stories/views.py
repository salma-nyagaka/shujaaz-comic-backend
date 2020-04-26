from rest_framework.generics import GenericAPIView
from .models import Stories, Characters
from .serializers import StoriesSerializer, CharacterSerializer
from rest_framework.response import Response
from rest_framework import status


class StoryAPIView(GenericAPIView):

    def get(self, request, comic_id):
        """Method for fetching a stories belonging to a comic"""
        stories = Stories.objects.filter(comic_id=comic_id)
        if not stories:
            return Response({
            "error": "This comic does not exist"},
            status=status.HTTP_404_NOT_FOUND)
        else:
            serializer = StoriesSerializer(stories, many=True)
            return Response({
                "status": "success",
                "message": "Successfully fetched this comic's stories",
                "data": serializer.data})


class CharactersAPIView(GenericAPIView):

    def get(self, request, story_id):
        """Method for fetching characters belonging to a story"""
        character = Characters.objects.filter(story_id=story_id)
        if not character:
            return Response({
            "error": "This story has no characters"},
            status=status.HTTP_404_NOT_FOUND)
        else:
            serializer = CharacterSerializer(character, many=True)
            return Response({
                "status": "success",
                "message": "Successfully fetched this characters in this story",
                "data": serializer.data})
