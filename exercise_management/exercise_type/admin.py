from django.contrib import admin
from exercise_type.models import StrengthTrainingRecord
from import_export.admin import ImportExportModelAdmin
from .resource import StrengthTrainingResource
from import_export.formats import base_formats


# class StrengthTrainingTypeAdmin(admin.ModelAdmin):
#     list_display = ('name',)


class StrengthTrainingRecordAdmin(ImportExportModelAdmin):
    resource_class = StrengthTrainingResource
    list_display = ('date', 'type', 'weight', 'repeat_times', 'memo')

    def get_export_formats(self):
        formats = (base_formats.CSV, )
        return [f for f in formats if f().can_export()]

    def get_import_formats(self):
        formats = (base_formats.XLSX,)
        return [f for f in formats if f().can_import()]


# admin.site.register(StrengthTrainingType, StrengthTrainingTypeAdmin)
admin.site.register(StrengthTrainingRecord, StrengthTrainingRecordAdmin)
