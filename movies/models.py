from django.db import models

# Create your models here.

class movies_model(models.Model):
    title= models.CharField(max_length= 50, unique= True)
    description = models.TextField()
    rate = models.FloatField(default=0.0)

    def __str__(self):
        return self.title
    

