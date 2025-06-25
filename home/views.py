from django.shortcuts import render
from home import models

# Create your views here.
def home(request):
    return render(request, "home/home.html")

def about(request):
    return render(request, "home/about.html")

def project(request):
    return render(request, "home/project.html")

def contact(request):
    if request.method == "POST":
        FullName = request.POST['Full Name']
        Email = request.POST['Email']
        YourMessage = request.POST['Your Message']
        # Use your Contact model from models, not a function named contact
        contact_obj = models.Contact(
            FullName=FullName,
            Email=Email,
            YourMessage=YourMessage
        )
        contact_obj.save()
        print("The data has been written to the db")

    return render(request, "home/contact.html")

