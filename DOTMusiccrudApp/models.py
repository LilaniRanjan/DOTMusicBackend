from django.utils import timezone
from django.db import models
from datetime import timedelta

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
    title = models.CharField(max_length=255)
    artist = models.ForeignKey('Artist', on_delete=models.CASCADE, related_name='songs')
    album = models.ForeignKey('Album', on_delete=models.SET_NULL, related_name='songs', blank=True, null=True)
    duration = models.DurationField()
    release_date = models.DateField(blank=True, null=True)
    genre = models.CharField(max_length=100, blank=True, null=True)
    audio_file = models.FileField(upload_to='songs/', blank=True, null=True)
    cover_image = models.ImageField(upload_to='songs_covers/', blank=True, null=True)
    lyrics = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def formatted_duration(self):
        if self.duration:
            total_seconds = int(self.duration.total_seconds())
            minutes, seconds = divmod(total_seconds, 60)
            return f"{minutes}:{seconds:02d}"
        return "0:00"

    class Meta:
        verbose_name = "Song"
        verbose_name_plural = "Songs"
        ordering = ['-release_date']

    def __str__(self):
        return self.title