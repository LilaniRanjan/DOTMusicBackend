from django.urls import path
from . import views

urlpatterns = [
    path('artists/', views.get_artists, name='get_artists'),
    path('albums/', views.get_albums, name='get_albums'),
    path('popular-radio/', views.get_popular_radio, name='get_popular_radio'),
]