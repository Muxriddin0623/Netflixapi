from django.views.generic import TemplateView
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.contrib import admin
from django.urls import path, include
from rest_framework.permissions import AllowAny

schema_view = get_schema_view(
    openapi.Info(
        title='Goodreads API',
        default_version='v1',
        description='Test Description',
        contact=openapi.Contact(email='muxriddin0623@gmail.com'),
        license=openapi.License(name='BSD License'),
    ),
    public=True,
    permission_classes=(AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Video.urls')),
    #path('swagger-ui/', TemplateView.as_view(
    #    template_name='swagger-ui.html',
    #    extra_context={'schema_url': 'openapi-schema'}
    #), name='swagger-ui'),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-docs'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
