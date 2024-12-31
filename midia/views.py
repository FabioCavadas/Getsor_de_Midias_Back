# Create your views here.
from rest_framework import status, viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .models import Media
from .serializers import MediaDetailSerializer, MediaSerializer


class BaseViewSet(viewsets.ModelViewSet):
    """
    Base ViewSet to handle common logic for different model ViewSets.
    """
    permission_class = [AllowAny]

    def get_permissions(self):
        if self.action == 'list' or self.action == 'retrieve':
            permission_classes = [AllowAny]
        # else:
        #     permission_classes = [ValidateUserAccess]

        return [permission() for permission in permission_classes]

    def retrieve(self, request, *args, **kwargs):
        """
        Handles the retrieval of a single instance, using the lookup_field.
        """
        instance = self.get_queryset().filter(**{self.lookup_field: self.kwargs[self.lookup_field]}).last()
        if instance is not None:
            serializer = self.get_serializer(instance)
            return Response(serializer.data)
        return Response({}, status=404)


class MediaViewSet(BaseViewSet):
    queryset = Media.objects.all()
    serializer_class = MediaDetailSerializer
    lookup_field = 'id'

    def get_queryset(self):
        if self.action == 'list':
            return Media.objects.filter(is_active=True)
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
