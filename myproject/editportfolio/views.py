from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from editportfolio.forms import EditPortfolio

# Create your views here.

@login_required
def portfolio(request):
  portfolioData = request.user.portfolio
  form = EditPortfolio(initial={'title': portfolioData.title,'description': portfolioData.description,'image': portfolioData.image,'LinkedIn': portfolioData.LinkedIn,'GitHub': portfolioData.GitHub},instance=request.user)
  if request.method == 'POST':
    form = EditPortfolio(request.POST, request.FILES, instance = request.user.portfolio)
    if form.is_valid():
      portfolioData.title = form.cleaned_data.get('title')
      portfolioData.description = form.cleaned_data.get('description')
      portfolioData.image = form.cleaned_data.get('image')
      portfolioData.LinkedIn = form.cleaned_data.get('LinkedIn')
      portfolioData.GitHub = form.cleaned_data.get('GitHub')

      portfolioData.save()
      request.user.save()
      
  return render(request, 'editportfolio/portfolio-edit.html', {'form': form})