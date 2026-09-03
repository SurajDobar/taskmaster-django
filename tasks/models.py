from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title= models.CharField( max_length=250)
    description = models.TextField()
    completed= models.BooleanField(default=False)
    id = models.AutoField(primary_key=True, unique=True, editable=False)
    def __str__(self):
        return self.title

    
