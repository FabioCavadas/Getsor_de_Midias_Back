from django.urls import path

from .views import MediaViewSet

urlpatterns = [
    path("midias/", MediaViewSet.as_view({"get": "list"})),
]
