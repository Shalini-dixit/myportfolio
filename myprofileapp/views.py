from django.shortcuts import render

# Create your views here.

def home_view(request):
    return render(request,'myprofileapp/home.html')

def about_view(request):
    return render(request,'myprofileapp/about.html')

def skills_view(request):
    return render(request,'myprofileapp/skills.html')

def projects_view(request):
    return render(request,'myprofileapp/projects.html')

def contact_view(request):
    return render(request,'myprofileapp/contact.html')
