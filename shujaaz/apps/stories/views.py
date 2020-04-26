from rest_framework.generics import GenericAPIView
from .models import Stories
from .serializers import StoriesSerializer
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

