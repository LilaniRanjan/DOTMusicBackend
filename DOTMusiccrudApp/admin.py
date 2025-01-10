from django.contrib import admin
from DOTMusiccrudApp.models import Artist

# Register your models here.
class ArtistAdmin(admin.ModelAdmin):
    list = ['name', 'bio', 'profile_picture', 'genre', 'created_at']

admin.site.register(Artist, ArtistAdmin)