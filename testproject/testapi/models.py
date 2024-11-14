from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(null=True,blank=True)

    def __str__(self):
        return self.name

class Note(models.Model):
    title =models.CharField(max_length=100)
    content = models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE, related_name="notes")

    def __str__(self):
        return self.title