from django.urls import path
from . import views

urlpatterns = [
  path('portfolio-edit/', views.CreatePortfolio.as_view(), name='portfolio-edit'),
]