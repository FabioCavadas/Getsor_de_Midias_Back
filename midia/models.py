from django.contrib.auth.models import User
from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    created_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, related_name="%(class)s_created_by")
    modified_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    modified_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, related_name="%(class)s_modified_by")

    class Meta:
        abstract = True


class Category(BaseModel):
    name = models.CharField(unique=True, max_length=100)

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

    def __str__(self):
        return self.name


class Media(BaseModel):
    IMAGE = 'image'
    VIDEO = 'video'

    MEDIA_TYPE_CHOICES = [
        (IMAGE, 'Image'),
        (VIDEO, 'Video'),
    ]
    category = models.ForeignKey(Category, related_name="Midias", on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    media_type = models.CharField(max_length=50, choices=MEDIA_TYPE_CHOICES, blank=True, null=True)

    class Meta:
        verbose_name = "Midia"
        verbose_name_plural = "Midias"

    def __str__(self):
        return self.name
