from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    bio = models.TextField(default="")
    date_of_birth  = models.DateField(null=True)
    
    @property
    def get_routes_uploaded(self):
        return self.route_set.count()
    
    def __str__(self):
        return self.username