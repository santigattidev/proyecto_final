from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpPortfolio(UserCreationForm):
  email = forms.EmailField()
  password1 = forms.CharField(label='Password',widget=forms.PasswordInput())
  password2 = forms.CharField(label='Confirm Password',widget=forms.PasswordInput())
  class Meta:
    model = User
    fields = ('username','email','password1','password2')
    help_texts = {k:None for k in fields}
  def clean_email(self):
    email = self.cleaned_data.get('email')
    username = self.cleaned_data.get('username')
    if User.objects.filter(email=email).exclude(username=username):
      raise forms.ValidationError(u'Email addresses must be unique.')
    return email