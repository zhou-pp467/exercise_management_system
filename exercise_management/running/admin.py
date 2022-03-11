from django.contrib import admin
from running.models import RunningRecord


class RunningRecordAdmin(admin.ModelAdmin):
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


admin.site.register(RunningRecord, RunningRecordAdmin)
