from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "home/home.html")

def about(request):
    return render(request, "home/about.html")

def project(request):
    return render(request, "home/project.html")

def contact(request):
    return render(request, "home/contact.html")

