# from django_restframework.serializers import serializer
from django.http import HttpResponse
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters, status

from .models import *
from .serializers import *


class MovieViewSet(ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    ordering_fields = ['imdb', 'genre']
    search_fields = ['imdb', 'genre', 'name']

    @action(detail=True, methods=["POST"])
    def add_actor(self, request, *args, **kwargs):
        actor_id = self.request.query_params("actor_id")
        actor = Actor.objects.get(id=actor_id)
        movie = actor.add(actor)
        serializer = MovieSerializer(movie)

        return Response(serializer.data)

    @action(detail=True, methods=["GET"])
    def remove_actor(self, request, *args, **kwargs):
        actor_id = self.request.query_params("actor_id")
        actor = Actor.objects.get(id=actor_id)
        movie = actor.remove(actor)
        serializer = MovieSerializer(movie)

        return Response(serializer.data)


class ActorViewSet(ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class MovieActorAPIView(APIView):
    @classmethod
    def get_extra_actions(cls):
        return []

    def get(self, request, *args, **kwargs):
        movie_id = self.request.query_params("movie_id")
        movie = Movie.objects.get(id=movie_id)
        actors = movie.actor.all()
        serializer = ActorSerializer(actors)

        return Response(serializer.data)


class MovieAPIView(APIView):
    def get(self, request):
        movie = Movie.objects.all()
        serializer = MovieSerializer(movie, many=True)

        return Response(data=serializer.data)

    def post(self, request):
        serializer = MovieSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(data=serializer.data)


class ActorAPIView(APIView):
    def get(self, request):
        actor = Actor.objects.all()
        serializer = ActorSerializer(actor, many=True)

        return Response(data=serializer.data)

    def post(self, request):
        serializer = ActorSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(data=serializer.data)


class CommentApiView(APIView):
    serializer_class = CommentSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    @classmethod
    def get_extra_actions(cls):
        return []

    def get_queryset(self):
        return Comment.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.validated_data['user'] = self.request.user
        serializer.save()

    def get(self, request):
        comment = Comment.objects.all()
        serializer = CommentSerializer(comment, many=True)

        return Response(data=serializer.data)

    def delete(self, request, *args, **kwargs):
        comment_id = self.request.query_params("comment_id")
        comment = Comment.objects.get(id=comment_id)
        comment.delete()

        return Response(comment, status=status.HTTP_204_NO_CONTENT)
