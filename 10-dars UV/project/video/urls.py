from django.urls import path, include
from .views import VideoViewSet
from rest_framework import routers


router = routers.DefaultRouter()

router.register('video', VideoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
