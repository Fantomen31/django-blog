from django.shortcuts import render
from django.contrib import messages
from .models import About
from .forms import CollaborateForm

# Create your views here.

def about_view(request):

    if request.method == "POST":
        collaborate_form = CollaborateForm(data=request.POST)
        if collaborate_form.is_valid():
            collaborate_form.save()
            messages.add_message(request, messages.SUCCESS, 
            "Collaboration request received! Awaiting audience with the emperor.")

    about = About.objects.all().order_by('-updated_on').first()
    collaborate_form = CollaborateForm()
    
    # Pass the latest_about content to the template
    return render(request, 'about/about.html', 
    {
        'about': about,
        'collaborate_form': collaborate_form
        },
    )
    