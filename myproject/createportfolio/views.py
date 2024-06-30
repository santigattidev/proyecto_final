from django.shortcuts import render
from django.views.generic.edit import CreateView
from . models import Portfolio

# Create your views here.
class CreatePortfolio(CreateView):
  model = Portfolio
  template_name = 'createportfolio/portfolio-edit.html'