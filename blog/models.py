from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User #this grabs the user from the Default django auth system
from django.urls import reverse


# Create your models here. these are database things

#Post class is everything needed to create a blog post here
class Post(models.Model): #new class that inherits from models
    title = models.CharField(max_length=100)
    content = models.TextField() # TextField is unrestricted text
    date_posted = models.DateTimeField(default=timezone.now) #import django util for default
    author = models.ForeignKey(User, on_delete=models.CASCADE) #grabs from Users table and what to do when user is deleted

    def __str__(self):
        return self.title

    def get_absolute_url(self): #this will return the url of the post you just made as a string and send you there
        return reverse('post-detail', kwargs={'pk': self.pk})
