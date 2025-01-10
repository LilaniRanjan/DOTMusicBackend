from django.shortcuts import render
from DOTMusiccrudApp.models import Album, Artist

# Combined view to retrieve both artists and albums
def retrieve_artist_and_album_view(request):
    artists = Artist.objects.all()
    albums = Album.objects.all()
    return render(request, 'DOTMusiccrudApp/index.html', {'artists': artists, 'albums': albums})
