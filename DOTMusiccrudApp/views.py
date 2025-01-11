from django.shortcuts import render
from DOTMusiccrudApp.models import Album, Artist, PopularRadio

# Combined view to retrieve both artists and albums
def retrieve_artist_album_view_and_popular_radio(request):
    artists = Artist.objects.all()
    albums = Album.objects.all()
    popular_radio = PopularRadio.objects.all()
    return render(request, 'DOTMusiccrudApp/index.html', {'artists': artists, 'albums': albums, 'popular_radio': popular_radio})
