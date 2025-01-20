from django.shortcuts import render
from rest_framework.viewsets import  ModelViewSet
from .serializers import movie_serializer
from .models import movies_model
# Create your views here.

class movie_viewset(ModelViewSet):
    queryset = movies_model.objects.all()
    serializer_class = movie_serializer