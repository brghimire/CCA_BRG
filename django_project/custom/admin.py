from django.contrib import admin
from .models.map_slug import MapSlugMapping
from .models.geography import Geography
from .models.category import Category
from .models.dataset import Dataset
from .models.dataset_file import DatasetFile


class MapSlugMappingAdmin(admin.ModelAdmin):
    list_display = ('map', 'slug')


class GeographyAdmin(admin.ModelAdmin):
    list_display = ('name', 'cca3', 'created_at', 'updated')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'name_long', 'created_at', 'updated')


class DatasetAdmin(admin.ModelAdmin):
    list_display = ('name', 'name_long', 'category', 'geography', 'created_at', 'updated')


class DatasetFileAdmin(admin.ModelAdmin):
    list_display = ('label', 'func', 'dataset', 'endpoint', 'created_at', 'updated')


admin.site.register(MapSlugMapping, MapSlugMappingAdmin)
admin.site.register(Geography, GeographyAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Dataset, DatasetAdmin)
admin.site.register(DatasetFile, DatasetFileAdmin)
