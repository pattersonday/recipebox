from django import forms
from .models import Recipe


class AuthorAddForm(forms.Form):

    name = forms.CharField(max_length=50)
    bio = forms.CharField(widget=forms.Textarea)


class RecipeAddForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = [
            'author',
            'title',
            'ingredients',
            'instructions',
            'time_required',
            'description',
        ]


form = RecipeAddForm()


class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)


class RecipeEditForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = [
            'title',
            'ingredients',
            'instructions',
            'time_required',
            'description',
        ]