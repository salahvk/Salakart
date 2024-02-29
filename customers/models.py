from django.db import models
from django.contrib.auth.models import User

class Customer (models.Model):
    Live = 1
    DELETE = 0
    DELETE_CHOICES = ((Live,'Live'),(DELETE,'Delete'))
    name = models.CharField(max_length=200)
    address = models.TextField()
    phone = models.CharField(max_length=10)
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name= 'customer_profile')
    delete_status = models.IntegerField(choices=DELETE_CHOICES,default = Live)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.name