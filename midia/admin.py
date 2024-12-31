# Register your models here.
from django import forms
from django.contrib import admin

from midia.models import Category, Media


class MediaForm(forms.ModelForm):

    def clean(self):
        data = self.cleaned_data
        category = data.get('category')
        media_type = data.get('media_type')

        # Validações no admin para garantir que 'categoria e tipo de mídia' sejam obrigatórias
        if not category:
            raise forms.ValidationError({
                'category': "Categoria é obrigatório.",
            })

        if not media_type:
            raise forms.ValidationError({
                'media_type': "Tipo de mídia é obrigatório."
            })

        return data


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

    def get_fields(self, request, obj):
        return ['name']


@admin.register(Media)
class MediaAdmin(admin.ModelAdmin):
    form = MediaForm
    list_display = ['name', 'category', 'media_type', 'is_active']
    list_filter = ['category', 'is_active']
    search_fields = ['name']
    ordering = ['category']

    def get_fields(self, request, obj):
        return ['category', 'name', 'media_type', 'media', 'is_active']
