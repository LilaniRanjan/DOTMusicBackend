from django.db import models

# Create your models here.
class Artist(models.Model):
    name = models.CharField(max_length=255)  # Name of the artist or band
    bio = models.TextField()  # Brief biography or description
    profile_picture = models.ImageField(upload_to='media/artist_Pic/', blank=True, null=True)  # Optional profile picture
    genre = models.CharField(max_length=100, blank=True, null=True)  # Optional genre
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically set the timestamp when the artist is created

class Album(models.Model):
    title = models.CharField(max_length=255)  # Title of the album
    artist = models.ForeignKey('Artist', on_delete=models.CASCADE, related_name='albums')  # Reference to the artist
    release_date = models.DateField()  # Release date of the album
    cover_image = models.ImageField(upload_to='media/album_covers/', blank=True, null=True)  # Optional cover image
    genre = models.CharField(max_length=100, blank=True, null=True)  # Optional genre
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically set when the album is created

class PopularRadio(models.Model):
    name = models.CharField(max_length=255) 
    description = models.TextField(blank=True, null=True)
    cover_image = models.ImageField(upload_to='media/radio_covers/', blank=True, null=True)
    rank = models.PositiveIntegerField()
    added_at = models.DateTimeField(auto_now_add=True)
