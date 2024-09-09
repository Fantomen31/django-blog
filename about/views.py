from django.shortcuts import render
from .models import About

# Create your views here.

def about_view(request):
    # Fetch the latest About content using the first() method
    latest_about = About.objects.order_by('-id').first()
    
    # Pass the latest_about content to the template
    return render(request, 'about/about.html', {'about': latest_about})