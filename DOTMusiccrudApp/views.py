from django.http import JsonResponse
from .models import Artist, Album, PopularRadio

def get_artists(request):
    artists = list(Artist.objects.values())
    return JsonResponse({'artists': artists}, safe=False)

def get_albums(request):
    albums = list(Album.objects.values())
    return JsonResponse({'albums': albums}, safe=False)

def get_popular_radio(request):
    radios = list(PopularRadio.objects.values())
    return JsonResponse({'popular_radio': radios}, safe=False)