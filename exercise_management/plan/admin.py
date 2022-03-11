from django.contrib import admin
from plan.models import RunningPlanItem, ExercisePlanItem


class RunningPlanItemAdmin(admin.ModelAdmin):
    list_display = ('date', 'memo')


class ExercisePlanItemAdmin(admin.ModelAdmin):
    list_display = ('date', 'type', 'memo')


admin.site.register(RunningPlanItem, RunningPlanItemAdmin)
admin.site.register(ExercisePlanItem, ExercisePlanItemAdmin)
