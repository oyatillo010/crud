from django.db import models
from django.urls import reverse

# Create your models here.
class Car(models.Model):
    name = models.CharField(max_length=50)
    year = models.IntegerField()
    img = models.TextField()
    cost = models.IntegerField()
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("home_detail", args={str(self.pk)})
    