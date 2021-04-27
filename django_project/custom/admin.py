from django.contrib import admin
from django.contrib.postgres import fields
from django_json_widget.widgets import JSONEditorWidget
from .models.geography import Geography
from .models.category import Category
from .models.dataset_file import DatasetFile


class MapSlugMappingAdmin(admin.ModelAdmin):
    list_display = ('map', 'slug')


class GeographyAdmin(admin.ModelAdmin):
    list_display = ('name', 'cca3', 'created_at', 'updated')
    formfield_overrides = {
        fields.JSONField: {'widget': JSONEditorWidget},
    }


class DatasetFileInline(admin.StackedInline):
    model = DatasetFile
    formfield_overrides = {
        fields.JSONField: {'widget': JSONEditorWidget},
    }

    class Media:
        js = ('/static/admin/js/show_geonode_layer.js', )


class DatasetFileAdmin(admin.ModelAdmin):
    list_display = (
        'category', 'label', 'func', 'geonode_layer', 'active'
    )


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'name_long', 'created_at', 'updated', 'get_total_files')

    def get_total_files(self, obj):
        return obj.datasetfile_set.count()

    get_total_files.short_description = 'Total Dataset Files'
    formfield_overrides = {
        fields.JSONField: {'widget': JSONEditorWidget},
    }
    inlines = [
        DatasetFileInline
    ]


admin.site.register(Geography, GeographyAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(DatasetFile, DatasetFileAdmin)
