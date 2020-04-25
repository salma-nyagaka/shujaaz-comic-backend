import os
import datetime
import jwt
from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import redirect
from django.template.loader import render_to_string
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly, \
    IsAuthenticated
from rest_framework.response import Response
from shujaaz.helpers.endpoint_response import get_success_responses


from shujaaz.apps.authentication.backends import JWTAuthentication
from .models import User
from .renderers import UserJSONRenderer
from .serializers import LoginSerializer



class LoginAPIView(GenericAPIView):
    permission_classes = (AllowAny,)
    renderer_classes = (UserJSONRenderer,)
    serializer_class = LoginSerializer

    def post(self, request):
        """Login a user"""
        email, password = request.data.get('email', None), request.data.get(
            'password', None)

        user = {"email": email, "password": password}
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        user_data = serializer.data

        user = User.get_user(user_data['email'])
        userdata = {
            "id": user.id,
            "email": user.email,
            "username": user.username,
            "first_name": user.first_name,
            "last_name": user.last_name,
        }
        user_data['token'] = \
            JWTAuthentication.generate_token(userdata=userdata)

        return get_success_responses(
            data=user_data,
            message="You have successfully logged in",
            status_code=status.HTTP_200_OK
        )

    def get(self):
        """Get a user"""
        return Response(
            data={
                "message": 'Only post requests are allowed to this endpoint.'
            })
