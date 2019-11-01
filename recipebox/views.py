from django.shortcuts import render, HttpResponseRedirect, reverse
from django.utils import timezone

from .models import Author, Recipe
from .forms import AuthorAddForm, RecipeAddForm

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


def author_form_view(request):
    html = 'generic_form.html'

    if request.method == 'POST':
        form = AuthorAddForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            Author.objects.create(
                name=data['name'],
                bio=data['bio']
            )
            return HttpResponseRedirect(reverse('homepage'))
    form = AuthorAddForm()

    return render(request, html, {'form': form})


def recipe_form_view(request):
    html = 'generic_form.html'

    if request.method == 'POST':
        form = RecipeAddForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            Recipe.objects.create(
                author=data['author'],
                title=data['title'],
                instructions=data['instructions'],
                time_required=data['time_required'],
                description=data['description'],
                post_date=timezone.now()
            )
            return HttpResponseRedirect(reverse('homepage'))

    form = RecipeAddForm()

    return render(request, html, {'form': form})
