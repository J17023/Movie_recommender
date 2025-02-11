from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UserModel

class UserSerializer(serializers.ModelSerializer):
    class Meta : 
        model = User
        fields =['username','email','password']
        extra_kwargs = {'password': {'write_only': True}}

class UserModelSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta : 
        model = UserModel
        fields =['user','bio','birth_date']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        #Se extrae los datos del user
        user_data = validated_data.pop('user')

        # Crear el User
        user = User.objects.create_user(
            username=user_data['username'],
            email=user_data['email'],
            password=user_data['password']
        )

        # Crear el UserModel asociado
        user_model = UserModel.objects.create(user=user, **validated_data)

        return user_model

