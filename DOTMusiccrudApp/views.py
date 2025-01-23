from django.http import JsonResponse
from .models import Artist, Album, PopularRadio, TodayInMusic, Songs

def get_lastfive_artists(request):
    artists = list(Artist.objects.order_by('-id')[:5].values())  # Fetch last 5 records
    return JsonResponse({'artists': artists}, safe=False)

def get_lastfive_albums(request):
    albums = list(Album.objects.order_by('-id')[:5].values())  # Fetch last 5 records
    return JsonResponse({'albums': albums}, safe=False)

def get_lastfive_popular_radio(request):
    radios = list(PopularRadio.objects.order_by('-id')[:5].values())  # Fetch last 5 records
    return JsonResponse({'popular_radio': radios}, safe=False)

def get_lastfive_today_in_music(request):
    today_in_music = list(TodayInMusic.objects.order_by('-id')[:5].values())  # Fetch last 5 records
    return JsonResponse({'today_in_music': today_in_music}, safe=False)

# --------------------------------------------------------------------------------------

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


# ---------------------------------------------------------------------------------------------

def get_songs_by_artist(request, artist_id):
    # Fetch songs where artist matches the given artist_id
    songs = list(Songs.objects.filter(artist_id=artist_id).values(
        'id', 'title', 'album__title', 'duration', 'release_date', 'genre', 'audio_file', 'lyrics'
    ))
    return JsonResponse({'songs': songs}, safe=False)