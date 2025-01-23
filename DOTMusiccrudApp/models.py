from django.utils import timezone
from django.db import models

# Create your models here.
class Artist(models.Model):
    name = models.CharField(max_length=255)  # Name of the artist or band
    bio = models.TextField()  # Brief biography or description
    profile_picture = models.ImageField(upload_to='artist_Pic/', blank=True, null=True)  # Optional profile picture
    genre = models.CharField(max_length=100, blank=True, null=True)  # Optional genre
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically set the timestamp when the artist is created

class Album(models.Model):
    title = models.CharField(max_length=255)  # Title of the album
    artist = models.ForeignKey('Artist', on_delete=models.CASCADE, related_name='albums')  # Reference to the artist
    release_date = models.DateField()  # Release date of the album
    cover_image = models.ImageField(upload_to='album_covers/', blank=True, null=True)  # Optional cover image
    genre = models.CharField(max_length=100, blank=True, null=True)  # Optional genre
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically set when the album is created

class PopularRadio(models.Model):
    name = models.CharField(max_length=255) 
    description = models.TextField(blank=True, null=True)
    cover_image = models.ImageField(upload_to='radio_covers/', blank=True, null=True)
    rank = models.PositiveIntegerField()
    added_at = models.DateTimeField(auto_now_add=True)
    

class TodayInMusic(models.Model):
    title = models.CharField(max_length=255)  # Headline for the event/news
    description = models.TextField()  # Detailed information about the event/news
    image = models.ImageField(upload_to='today_music/', blank=True, null=True)
    event_date = models.DateField(default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)


class Songs(models.Model):
    title = models.CharField(max_length=255)  # Title of the song
    artist = models.ForeignKey('Artist', on_delete=models.CASCADE, related_name='songs')  # Reference to the artist
    album = models.ForeignKey('Album', on_delete=models.SET_NULL, related_name='songs', blank=True, null=True)  # Optional reference to the album
    duration = models.DurationField()  # Duration of the song
    release_date = models.DateField()  # Release date of the song
    genre = models.CharField(max_length=100, blank=True, null=True)  # Optional genre
    audio_file = models.FileField(upload_to='songs/', blank=True, null=True)  # Optional audio file upload
    lyrics = models.TextField(blank=True, null=True)  # Optional lyrics of the song
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically set when the song is created


