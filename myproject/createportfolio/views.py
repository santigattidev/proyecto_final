from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from . models import Portfolio
from . forms import SignUpPortfolio
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login as django_login

# Create your views here.
# class CreatePortfolio(CreateView):
#   model = Portfolio
#   template_name = 'createportfolio/portfolio-edit.html'
#   success_url = '/'
#   fields = '__all__'

def createUser(request):
  form = SignUpPortfolio()
  if request.method == 'POST':
    form = SignUpPortfolio(request.POST)
    if form.is_valid():
      form.save()
      # redirect('portfolio-edit')
  return render(request, 'createportfolio/portfolio-signup.html', {'form': form})

def login(request):
  form = AuthenticationForm()
  if request.method == 'POST':
    form = AuthenticationForm(request=request, data=request.POST)
    if form.is_valid():
      username = form.cleaned_data.get('username')
      password = form.cleaned_data.get('password')
      user = authenticate(username=username, password=password)
      if user is not None:
        django_login(request, user)
        return redirect('index')
  return render(request, 'createportfolio/portfolio-login.html', {'form': form})