from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Portfolio(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  User.email = models.EmailField()
  User.username = models.CharField(max_length=100)
  title = models.CharField(max_length=200)
  description = models.TextField()
  image = models.ImageField(upload_to='portfolio/images/', null=True, blank=True)
  LinkedIn = models.URLField(blank=True)
  GitHub = models.URLField(blank=True)

  def __str__(self):
    return self.title