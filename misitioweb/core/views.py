from django.shortcuts import render, HttpResponse
from django.templatetags.static import static
from django.shortcuts import render

def index(request):
    return render(request, 'core/index.html')

def about_view(request):
    return render(request, 'core/about.html')
