from django.db import models
from django.utils import timezone

class Post(models.Model):
    blog_title = models.CharField(max_length=200)
    blog_date = models.DateTimeField()
    blog_text = models.TextField()
    blog_image = models.ImageField(upload_to="blog_images/")
# Create your models here.
