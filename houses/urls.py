from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter
from rest_framework.schemas import get_schema_view

from . import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'houses', views.HouseViewSet)

schema_view = get_schema_view(title='Houses API')


urlpatterns = [
    path('', include(router.urls)),
    path('schema/', schema_view),
]