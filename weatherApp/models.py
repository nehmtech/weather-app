from django.db import models

# Create your models here.

class Weather(models.Model):
    location = models.CharField(max_length=150)
    temperature = models.DecimalField(max_digits=5, decimal_places=2)
    humidity = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField()
    
    def __str__(self):
        return self.location
    