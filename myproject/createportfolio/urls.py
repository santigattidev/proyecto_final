from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView as django_logout

urlpatterns = [
  path('signup/', views.createUser, name='signup'),
  path('login/', views.login, name='login'),
  path('logout/', django_logout.as_view(template_name='createportfolio/portfolio-logout.html'), name='logout'),
]