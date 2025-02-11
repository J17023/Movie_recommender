from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from .models import UserModel
from .serializers import UserModelSerializer

# Create your views here.

class RegisterCreateView(generics.CreateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserModelSerializer

    