from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser): 
    name = models.CharField(max_length=225, null=False, blank=False) 
    password = models.CharField(max_length=225, null=False, blank=False)
    email = models.EmailField(max_length=225, unique=True)
    
    first_name = None 
    last_name = None 
    username = None 

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    