from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.CharField(max_length = 50)
    phone = models.CharField(max_length=50)
    


    def __unicode__(self):
        return self.username