from django.contrib import admin
from DOTMusiccrudApp.models import Album, Artist

# Register your models here.
class ArtistAdmin(admin.ModelAdmin):
    list = ['name', 'bio', 'profile_picture', 'genre', 'created_at']

admin.site.register(Artist, ArtistAdmin)

class AlbumAdmin(admin.ModelAdmin):
    list = ['title', 'artist', 'release_date', 'cover_image', 'genre', 'created_at']

admin.site.register(Album, AlbumAdmin)