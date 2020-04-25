from django.urls import path

app_name = "comic"

from .views import ComicAPIView, SingleComicAPIView


urlpatterns = [
    path('comics/', ComicAPIView.as_view(),
         name='comics'),
    path('comics/<str:comic_id>/', SingleComicAPIView.as_view(),
         name='specific_comic'),

]
