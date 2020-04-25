from django.urls import path

from django.views.decorators.cache import cache_page


app_name = "authentication"

from .views import (
    LoginAPIView
)

urlpatterns = [
    path('users/login', LoginAPIView.as_view(),
         name='user_login'),
]
