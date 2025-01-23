# Create your views here.
from rest_framework import status, viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .models import Media
from .serializers import MediaDetailSerializer, MediaSerializer


class MediaViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = Media.objects.all()
    serializer_class = MediaDetailSerializer
    lookup_field = 'id'

    def get_queryset(self):
        if self.action == 'list':
            if self.request.user.is_authenticated:
                return Media.objects.filter(is_active=True)
            return Media.objects.filter(is_active=True, media_type="image")
        return super().get_queryset()

    def get_serializer_class(self):
        if self.action in "list":
            return MediaSerializer
        return super().get_serializer_class()

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.is_active = False
        instance.save()
        return Response({}, status=status.HTTP_204_NO_CONTENT)
