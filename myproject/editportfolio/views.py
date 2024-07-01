from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from editportfolio.forms import Portfolio
# Create your views here.

@login_required
def portfolio(request):
  form = Portfolio()
  if request.method == 'POST':
    form = Portfolio(request.POST, request.FILES, instance = request.user.portfolio)
    if form.is_valid():
      image = form.cleaned_data.get('image')
      portfolioData = request.user.portfolio
      portfolioData.image = image
      portfolioData.save()
      form.save()
      
  return render(request, 'editportfolio/portfolio-edit.html')