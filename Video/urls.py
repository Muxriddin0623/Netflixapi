from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter

from .views import *

router = DefaultRouter()
# todo_router = DefaultRouter()
router.register('movie', MovieViewSet)
#router.register('actors', ActorViewSet)
#router.register('movies', MovieActorAPIView, "movies")
router.register('comment', CommentApiView, "comment")

urlpatterns = [
    #path('movies/<int:id>/actors', MovieActorAPIView.as_view(), name='movies'),
    #path('actors/', ActorAPIView.as_view(), name='actor'),
    path("comment/", include(router.urls)),
    path('auth/', obtain_auth_token),
    path('', include(router.urls))
]
