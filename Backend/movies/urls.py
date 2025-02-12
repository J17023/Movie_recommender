from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import movie_viewset

router = DefaultRouter()
router.register(r'movies',movie_viewset)

urlpatterns = [
    path('',include(router.urls)),
]
