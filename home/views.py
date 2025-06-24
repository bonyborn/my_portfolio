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
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        concern = request.POST['concern']
    #print(name, email, phone, desc)
    ins = Contact (name=name, email=email, phone=phone, concern=concern)
    ins.save()
    print("The data has been weitten to the db")

    return render(request, "home/contact.html")

