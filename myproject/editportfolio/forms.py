from django import forms
from django.contrib.auth.forms import UserChangeForm
from . models import Portfolio

class EditPortfolio(UserChangeForm):
  password = None
  first_name = forms.CharField(required=False)
  last_name = forms.CharField(required=False)
  email = forms.EmailField(required=False)
  title = forms.CharField(required=False)
  description = forms.CharField(required=False)
  image = forms.ImageField(required=False)
  LinkedIn = forms.URLField(required=False)
  GitHub = forms.URLField(required=False)
  class Meta:
    model = Portfolio
    fields = ['first_name','last_name','email','title','description','image','LinkedIn','GitHub']
    help_texts = {k:None for k in fields}