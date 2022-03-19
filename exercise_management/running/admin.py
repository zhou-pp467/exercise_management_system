from django.contrib import admin
from running.models import RunningRecord
from import_export.admin import ImportExportModelAdmin
from .resource import RunningResource
from import_export.formats import base_formats


class RunningRecordAdmin(ImportExportModelAdmin):
    resource_class = RunningResource
    list_display = ('date', 'speed', 'pace', 'step_frequency', 'step_length',
                    'heart_rate_average', 'heart_rate_max', 'memo')
    exclude = ('step_length',)

    def save_model(self, request, obj, form, change):
        if obj.pace is None:
            obj.pace = 60 / obj.speed
        if obj.speed is None:
            obj.speed = 60 / obj.pace
        obj.step_length = round(1000 / (obj.pace * obj.step_frequency), 2)
        super().save_model(request, obj, form, change)

    def get_export_formats(self):
        formats = (base_formats.CSV, )
        return [f for f in formats if f().can_export()]

    def get_import_formats(self):
        formats = (base_formats.XLSX,)
        return [f for f in formats if f().can_import()]


admin.site.register(RunningRecord, RunningRecordAdmin)
