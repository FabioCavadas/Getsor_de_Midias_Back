from django.urls import path

from .views import MediaViewSet

urlpatterns = [
    path("Midias/", MediaViewSet.as_view({"get": "list"})),
]
