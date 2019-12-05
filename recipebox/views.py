from django.shortcuts import render, HttpResponseRedirect, reverse
from django.utils import timezone
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .models import Author, Recipe
from .forms import AuthorAddForm, LoginForm, RecipeAddForm, RecipeEditForm


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


def recipe_favorite_view(request, id):
    favorite = Recipe.objects.get(id=id)
    current_user= Author.objects.get(user=request.user)

    current_user.favorite.add(favorite)
    current_user.save() 

    return HttpResponseRedirect(reverse('homepage'))


def recipe_view(request, id):
    html = 'recipe.html'

    recipe = Recipe.objects.filter(id=id)

    return render(request, html, {'recipe': recipe})


@login_required
def author_form_view(request):
    html = 'generic_form.html'

    if request.method == 'POST':
        form = AuthorAddForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            u = User.objects.create_user(
                username=data['name'],
                password=data['password']
            )
            Author.objects.create(
                user=u,
                name=data['name'],
                bio=data.get['bio']
            )
            return HttpResponseRedirect(reverse('homepage'))

    form = AuthorAddForm()

    return render(request, html, {'form': form})


@login_required
def recipe_form_view(request):
    html = 'generic_form.html'

    if request.method == 'POST':
        form = RecipeAddForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            Recipe.objects.create(
                author=data['author'],
                title=data['title'],
                ingredients=data['ingredients'],
                instructions=data['instructions'],
                time_required=data['time_required'],
                description=data['description'],
                post_date=timezone.now()
            )
            return HttpResponseRedirect(reverse('homepage'))

    form = RecipeAddForm()

    return render(request, html, {'form': form})


def login_view(request):
    html = 'login_form.html'

    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                username=data['username'],
                password=data['password']
            )
            if user:
                login(request, user)
                return HttpResponseRedirect(
                    request.GET.get('next', reverse('homepage')))

    form = LoginForm()

    return render(request, html, {'form': form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('homepage'))





@login_required
def edit_recipe_view(request, id):
    html = 'edit.html'

    instance = Recipe.objects.get(id=id)

    if request.method == 'POST':
        form = RecipeEditForm(
            request.POST,
            instance=instance
            )
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('homepage'))
    else: 
        data = {
            'title': instance.title,
            'ingredients': instance.ingredients,
            'instructions': instance.instructions,
            'time_required': instance.time_required,
            'description': instance.description,
            }
        form = RecipeEditForm(initial=data)
        

    return render(request, html, {'form': form, 'recipe':instance})
