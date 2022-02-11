from django.shortcuts import render

# Create your views here.

def home_view(request):
    return render(request, "home/home.html")
def about_view(request):
    return render(request, "home/about.html")
def contact_view(request):
    return render(request, "home/contact.html")