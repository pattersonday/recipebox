from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    bio = models.TextField(blank=True, null=True)
    favorite = models.ManyToManyField('Recipe', blank=True, related_name='D_favorite')


    def __str__(self):
        return self.name


class Recipe(models.Model):
    author = models.ForeignKey('Author', on_delete=models.CASCADE, related_name='D_author')
    title = models.CharField(max_length=100)
    ingredients = models.TextField(default='')
    instructions = models.TextField()
    time_required = models.IntegerField(default=1)
    description = models.TextField()
    post_date = models.DateTimeField(default=timezone.now)
    


    def __str__(self):
        return f'{self.title} - {self.author.name}'
