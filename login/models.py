from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank = True, null = True)
    #avatar = ima
    birth_date  = models.DateField(blank = True , null= True)


    def __str__(self):
        return f"Perfil de {self.user.username}"
    
    class Meta:
        verbose_name = "Perfil de usuario"
        verbose_name_plural = "Perfiles de usuarios"