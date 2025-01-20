from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ModelViewSet

router = DefaultRouter()
router.register(r'movies', ModelViewSet, basename='movie')

urlpatterns = [
    path('',include(router.urls)),
]
