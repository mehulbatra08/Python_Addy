from django.db import models

# Create your models here.

class names(models.Model):
    First_name = models.CharField(max_length=30)
    Last_name = models.CharField(max_length=30)

    def __str__(self):
        return self.First_name

    
