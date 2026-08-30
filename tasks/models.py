from django.db import models

# Create your models here.

class Task(models.Model):
    title= models.CharField( max_length=250)
    description = models.TextField()
    completed= models.BooleanField(default=False)
    id = models.AutoField(primary_key=True, unique=True, editable=False)
    def __str__(self):
        return self.title

    
