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
                "message": "These are the Comics available",
                "data": serializer.data})


class SingleComicAPIView(GenericAPIView):

     def get(self, request, comic_id):
        """Method for fetching a single comic."""
        try:
            comic = Comic.get_comic_by_id(comic_id=comic_id)
            serializer = ComicSerializer(comic)
            return Response({
                "status": "success",
                "message": "Successfully fetched the comic book",
                "data": serializer.data})
        except (KeyError, Comic.DoesNotExist):
            return Response({
                "error": "This comic does not exist"},
                status=status.HTTP_404_NOT_FOUND)