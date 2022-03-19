from django.contrib import admin
from plan.models import RunningPlanItem, ExercisePlanItem
from import_export.admin import ImportExportModelAdmin
from .resource import RunningPlanResource, ExercisePlanResource
from import_export.formats import base_formats


class RunningPlanItemAdmin(ImportExportModelAdmin):
    resource_class = RunningPlanResource
    list_display = ('date', 'memo')

    def get_export_formats(self):
        formats = (base_formats.CSV, )
        return [f for f in formats if f().can_export()]

    def get_import_formats(self):
        formats = (base_formats.XLSX,)
        return [f for f in formats if f().can_import()]


class ExercisePlanItemAdmin(ImportExportModelAdmin):
    resource_class = ExercisePlanResource
    list_display = ('date', 'type', 'memo')

    def get_export_formats(self):
        formats = (base_formats.CSV, )
        return [f for f in formats if f().can_export()]

    def get_import_formats(self):
        formats = (base_formats.XLSX,)
        return [f for f in formats if f().can_import()]


admin.site.register(RunningPlanItem, RunningPlanItemAdmin)
admin.site.register(ExercisePlanItem, ExercisePlanItemAdmin)
