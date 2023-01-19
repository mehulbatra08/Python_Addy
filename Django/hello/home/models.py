from django.db import models

class Contactus(models.Model):
    mypassword = models.CharField(max_length =122)
    myemail = models.CharField(max_length =122)
    
    def __str__(self):
        return self.myemail


