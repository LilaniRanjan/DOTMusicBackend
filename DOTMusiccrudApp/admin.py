from django.contrib import admin
from DOTMusiccrudApp.models import Album, Artist, PopularRadio, TodayInMusic, Songs

# Register your models here.
class ArtistAdmin(admin.ModelAdmin):
    list = ['name', 'bio', 'profile_picture', 'genre', 'created_at']

admin.site.register(Artist, ArtistAdmin)


class AlbumAdmin(admin.ModelAdmin):
    list = ['title', 'artist', 'release_date', 'cover_image', 'genre', 'created_at']

admin.site.register(Album, AlbumAdmin)


class PopularRadiodmin(admin.ModelAdmin):
    list = ['name', 'description', 'cover_image', 'rank', 'added_at']

admin.site.register(PopularRadio, PopularRadiodmin)


class TodayInMusicAdmin(admin.ModelAdmin):
    list = ['title', 'description', 'image', 'event_date', 'created_at']

admin.site.register(TodayInMusic, TodayInMusicAdmin)

class SongsAdmin(admin.ModelAdmin):
    list_display = ['title', 'artist', 'album', 'duration', 'release_date', 'genre', 'audio_file', 'lyrics', 'created_at']

admin.site.register(Songs, SongsAdmin)
