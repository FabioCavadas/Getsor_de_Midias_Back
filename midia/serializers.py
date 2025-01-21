from rest_framework import serializers

from .models import Category, Media


class MediaSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), required=True)
    category_name = serializers.SerializerMethodField()

    class Meta:
        model = Media
        fields = ["id", "name", "is_active", "category", "category_name", "media", "media_type"]

    def get_category_name(self, obj):
        return obj.category.name


class MediaDetailSerializer(MediaSerializer):
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), required=True)
    category_name = serializers.SerializerMethodField()
    is_active = serializers.BooleanField(required=False, default=True)

    class Meta:
        model = Media
        fields = ["id", "name", "is_active", "category", "category_name", "media", "media_type"]

    def get_category_name(self, obj):
        return obj.category.name

    def deactivate_unmentioned_apps(self, existing_apps, requested_app_ids):
        for existing_app in existing_apps:
            if existing_app.id not in requested_app_ids:
                existing_app.is_active = False
                existing_app.save()
