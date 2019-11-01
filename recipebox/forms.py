from django import forms
from .models import Author, Recipe


class AuthorAddForm(forms.Form):

    name = forms.CharField(max_length=50)
    bio = forms.CharField(widget=forms.Textarea)


class RecipeAddForm(forms.ModelForm):

    # author = forms.ModelChoiceField(queryset=Author.objects.all())
    # title = forms.CharField(max_length=100)
    # ingredients = forms.CharField(widget=forms.Textarea)
    # instructions = forms.CharField(widget=forms.Textarea)
    # time_required = forms.CharField(widget=forms.NumberInput)
    # description = forms.CharField(widget=forms.Textarea)
    # post_date = forms.CharField(widget=forms.DateTimeInput)
