from django.contrib import admin

from . import models


class SchemaAdmin(admin.ModelAdmin):

    list_display = ('id', 'title', 'separator', 'quotes', 'slug', 'user', 'edited_at')
    list_display_links = ('title',)
    search_fields = ('title', 'user', 'edited_at')
    list_filter = ('title', 'user', 'edited_at')


admin.site.register(models.Schema, SchemaAdmin)


class ColumnAdmin(admin.ModelAdmin):

    list_display = ('id', 'header', 'order', 'type', 'start_integer', 'end_integer', 'sentences', 'schema')
    list_display_links = ('id',)
    search_fields = ('header', 'schema', 'type')
    list_filter = ('header', 'schema', 'type')


admin.site.register(models.Column, ColumnAdmin)


class DataSetAdmin(admin.ModelAdmin):

    list_display = ('id', 'rows_quantity', 'generated_at', 'csv_file', 'is_uploaded', 'schema')
    list_display_links = ('id',)
    search_fields = ('rows_quantity', 'generated_at', 'is_uploaded', 'schema')
    list_filter = ('is_uploaded', 'schema', 'rows_quantity', 'generated_at')


admin.site.register(models.DataSet, DataSetAdmin)
