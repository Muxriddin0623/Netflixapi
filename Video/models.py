from django.contrib.auth.models import User
from django.db import models


class Actor(models.Model):
    name = models.CharField(max_length=200, blank=False)
    birthdate = models.DateField(blank=False)
    genre = models.CharField(max_length=150)


class Movie(models.Model):
    name = models.CharField(max_length=200, blank=False)
    year = models.IntegerField(blank=False)
    imdb = models.IntegerField(blank=False)
    genre = models.CharField(max_length=150)
    actor = models.ManyToManyField(Actor)


class Comment(models.Model):
    movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(max_length=150, blank=True)
    created_date = models.DateField(auto_now_add=True, blank=False)
