from django.shortcuts import render

# Create your views here.
# home views
def home(request):
    return render(request, 'portfolio/home.html')