from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from PIL import Image

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nsu_id = models.IntegerField(null = True)
    image = models.ImageField(default='profile_pics/default.jpg', upload_to='profile_pics')
    status = models.CharField(max_length = 100, default = 'Status')
    bio = models.TextField(default = 'Bio')
    date_registered = models.DateTimeField(default=timezone.now)
    fb_link = models.URLField(default = 'https://www.facebook.com/')
    insta_link = models.URLField(default = 'https://www.instagram.com/')
    git_link = models.URLField(default = 'https://github.com/')
    linkedin_link = models.URLField(default = 'https://bd.linkedin.com/')
    twitter_link = models.URLField(default = 'https://twitter.com/')

    def __str__(self):
        return f'{self.user.username} Profile'

    def get_absolute_url(self):
        return reverse('user-detail', kwargs={'pk': self.pk})

class Student(models.Model):
    name = models.CharField(max_length = 50)
    id = models.IntegerField(primary_key=True)
    email = models.EmailField(unique = True)
