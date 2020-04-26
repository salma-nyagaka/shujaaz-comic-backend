from django.urls import path

app_name = "stories"

from .views import StoryAPIView, CharactersAPIView


urlpatterns = [
    path('comics/<str:comic_id>/stories/', StoryAPIView.as_view(),
         name='stories'),
    path('story/<str:story_id>/characters/', CharactersAPIView.as_view(),
         name='characters'),

]
