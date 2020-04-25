from rest_framework.generics import GenericAPIView
from .models import Comic
from .serializers import ComicSerializer
from rest_framework.response import Response
from rest_framework import status


class ComicAPIView(GenericAPIView):

    def get(self, request):
        """Method for fetching all comics."""
        comic = Comic.objects.all()
        serializer = ComicSerializer(comic, many=True)
        return Response({
                "status": "success",
                "message": "These are the Comic available",
                "data": serializer.data})


class SingleComicAPIView(GenericAPIView):

     def get(self, request, user_id):
        """Method for fetching a single comic."""
        try:
            comic = User.get_user_by_id(user_id=user_id)
            serializer = ComicSerializer(comic)
            return Response({
                "status": "success",
                "message": "Successfully fetched the comic book",
                "data": serializer.data})
        except (KeyError, Comic.DoesNotExist):
            return Response({
                "error": "This comic does not exist"},
                status=status.HTTP_404_NOT_FOUND)