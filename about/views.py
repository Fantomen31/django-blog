from django.shortcuts import render
from .models import About

# Create your views here.

def about_view(request):
    # Fetch the latest About content using the first() method
    about = About.objects.all().order_by('-updated_on').first()
    
    # Pass the latest_about content to the template
    return render(request, 'about/about.html', {'about': about})