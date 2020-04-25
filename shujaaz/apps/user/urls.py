from django.urls import path


app_name = "user"

from .views import UserAPIView, SingleUserAPIView


urlpatterns = [
    path('users/', UserAPIView.as_view(),
         name='content_creator'),
    path('users/<str:user_id>/', SingleUserAPIView.as_view(),
         name='specific_content_creator'),

]
