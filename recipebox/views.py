from django.shortcuts import render

from .models import Author, Recipe

# Create your views here.


def index(request):
    html = 'index.html'

    recipes = Recipe.objects.all()

    return render(request, html, {'data': recipes})


def author_view(request, id):
    html = 'author.html'

    author = Author.objects.filter(id=id)

    author_recipe = Recipe.objects.filter(author=id)

    return render(request, html,
                  {'author': author, 'author_recipe': author_recipe})


def recipe_view(request, id):
    html = 'recipe.html'

    recipe = Recipe.objects.filter(id=id)

    return render(request, html, {'recipe': recipe})