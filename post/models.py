from django.db import models
from django.urls import reverse
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=150)
    text = models.TextField()
    name =models.CharField(max_length=100,blank=True)

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('home')