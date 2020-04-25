from django.shortcuts import render

# Create your views here.
from rest_framework.generics import GenericAPIView
from .models import User
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework import status


class UserAPIView(GenericAPIView):

    def get(self, request, format=None):
        """ Method for fetching all crators"""
        user = User.objects.all()
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data)

class SingleUserAPIView(GenericAPIView):
     def get(self, request, user_id):
        """
        Method for fetching a single creator
        """
        try:
            user = User.get_user_by_id(user_id=user_id)
            serializer = UserSerializer(user)
   
            return Response({
                "status": "success",
                "message": "hey",
                "data": serializer.data})
        except (KeyError, User.DoesNotExist):
            return Response({
                "error": "This user does not exist"},
                status=status.HTTP_404_NOT_FOUND)