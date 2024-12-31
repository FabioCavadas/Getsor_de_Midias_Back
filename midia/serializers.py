from rest_framework import serializers

from .models import Category, Media


class MediaSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), required=True)

    class Meta:
        model = Media
        fields = ["id", "name", "is_active", "category"]


class MediaDetailSerializer(MediaSerializer):
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), required=True)
    is_active = serializers.BooleanField(required=False, default=True)

    class Meta:
        model = Media
        fields = ["id", "name", "is_active", "category"]

    def deactivate_unmentioned_apps(self, existing_apps, requested_app_ids):
        for existing_app in existing_apps:
            if existing_app.id not in requested_app_ids:
                existing_app.is_active = False
                existing_app.save()
