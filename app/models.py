from django.db import models

class User(models.Model):
    name=models.CharField(max_length=50)
    phone=models.CharField(max_length=12)
    address=models.CharField(max_length=100)
    password=models.CharField(max_length=30)
    
    def __str__(self) -> str:
        return self.name