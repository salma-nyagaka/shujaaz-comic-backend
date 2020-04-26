from django.urls import path

app_name = "stories"

from .views import StoryAPIView


urlpatterns = [
    path('comics/<str:comic_id>/stories/', StoryAPIView.as_view(),
         name='stories'),

]
