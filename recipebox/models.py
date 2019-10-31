from django.db import models

# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=50)
    bio = models.TextField()

    def __str__(self):
        return self.name


class Recipe(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    instructions = models.TextField()
    time_required = models.IntegerField(default=1)
    description = models.TextField()
    # post_date = models.DateTimeField(default=1)

    def __str__(self):
        return f'{self.title} - {self.author.name}'
