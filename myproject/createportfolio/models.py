from django.db import models

# Create your models here.
class Portfolio(models.Model):
  name = models.CharField(max_length=100)
  about_me = models.CharField(max_length=300)
  avatar = models.ImageField(upload_to='portfolio/images/')
  LinkedIn = models.URLField(blank=True)
  GitHub = models.URLField(blank=True)