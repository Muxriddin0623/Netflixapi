from rest_framework import serializers
from rest_framework.validators import ValidationError
from .models import *


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id', 'name', 'year', 'imdb', 'genre', 'actor')


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ('id', 'name', 'birthdate', 'genre')

    def validate_birthdate(self, value):

        if value.year < 1950:
            raise ValidationError('Erroorrr')
        return value


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'user_id', 'movie_id', 'text', 'created_date')
