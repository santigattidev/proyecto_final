from django import forms
from django.contrib.auth.forms import UserChangeForm
from . models import Portfolio

class EditPortfolio(UserChangeForm):
  password = None
  email = forms.EmailField(required=False)
  username = forms.CharField(required=False)
  title = forms.CharField(required=False)
  description = forms.CharField(required=False)
  image = forms.ImageField(required=False)
  LinkedIn = forms.URLField(required=False)
  GitHub = forms.URLField(required=False)
  class Meta:
    model = Portfolio
    fields = ['email', 'username', 'title', 'description', 'image', 'LinkedIn', 'GitHub']
    help_texts = {k:None for k in fields}