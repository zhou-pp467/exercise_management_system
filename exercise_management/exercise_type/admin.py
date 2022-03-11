from django.contrib import admin
from exercise_type.models import StrengthTrainingRecord


# class StrengthTrainingTypeAdmin(admin.ModelAdmin):
#     list_display = ('name',)


class StrengthTrainingRecordAdmin(admin.ModelAdmin):
    list_display = ('date', 'type', 'weight', 'repeat_times', 'memo')


# admin.site.register(StrengthTrainingType, StrengthTrainingTypeAdmin)
admin.site.register(StrengthTrainingRecord, StrengthTrainingRecordAdmin)