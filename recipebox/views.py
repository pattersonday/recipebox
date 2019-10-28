from django.shortcuts import render

from .models import Recipe

# Create your views here.


def index(request):
    html = 'index.html'

    recipes = Recipe.objects.all()

    return render(request, html, {'data': recipes})