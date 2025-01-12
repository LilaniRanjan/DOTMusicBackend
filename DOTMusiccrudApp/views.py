from django.http import JsonResponse
from .models import Artist, Album, PopularRadio, TodayInMusic

def get_artists(request):
    artists = list(Artist.objects.values())
    return JsonResponse({'artists': artists}, safe=False)

def get_albums(request):
    albums = list(Album.objects.values())
    return JsonResponse({'albums': albums}, safe=False)

def get_popular_radio(request):
    radios = list(PopularRadio.objects.values())
    return JsonResponse({'popular_radio': radios}, safe=False)

def get_today_in_music(request):
    today_in_music = list(TodayInMusic.objects.values())
    return JsonResponse({'today_in_music': today_in_music}, safe=False)