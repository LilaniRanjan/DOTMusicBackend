from django.shortcuts import render
from DOTMusiccrudApp.models import Artist

# Create your views here.

def retrive_Artist_view(request):
    artist = Artist.objects.all()
    return render(request, 'DOTMusiccrudApp/index.html',{'artist':artist})