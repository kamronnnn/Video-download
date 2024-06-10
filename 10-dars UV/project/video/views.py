from django.shortcuts import render
from .serializers import VideoSerializer
from .models import Video
from rest_framework import viewsets

# Create your views here.


class VideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
