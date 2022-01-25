from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required

def index(request):
    return render(request, "client/index.html")

def about(request):
    return render(request,"client/about.html")

def contact(request):
    return render(request,"client/contact.html")

def gallery(request):
    return render(request,"client/gallery.html")

def services(request):
    return render(request,"client/services.html")

def typography(request):
    return render(request,"client/typography.html")
