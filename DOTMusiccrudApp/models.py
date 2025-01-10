from django.db import models

# Create your models here.
class Artist(models.Model):
    name = models.CharField(max_length=255)  # Name of the artist or band
    bio = models.TextField()  # Brief biography or description
    profile_picture = models.ImageField(upload_to='media/artist_Pic/', blank=True, null=True)  # Optional profile picture
    genre = models.CharField(max_length=100, blank=True, null=True)  # Optional genre
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically set the timestamp when the artist is created
