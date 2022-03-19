# by zhou_pp
from import_export import resources
from import_export.fields import Field
from running.models import RunningRecord


class RunningResource(resources.ModelResource):
    date = Field(attribute='date', column_name=RunningRecord.date.field.verbose_name)
    speed = Field(attribute='speed', column_name=RunningRecord.speed.field.verbose_name)
    pace = Field(attribute='pace', column_name=RunningRecord.pace.field.verbose_name)
    step_frequency = Field(attribute='step_frequency', column_name=RunningRecord.step_frequency.field.verbose_name)
    step_length = Field(attribute='step_length', column_name=RunningRecord.step_length.field.verbose_name)
    heart_rate_average = Field(attribute='heart_rate_average',
                               column_name=RunningRecord.heart_rate_average.field.verbose_name)
    heart_rate_max = Field(attribute='heart_rate_max', column_name=RunningRecord.heart_rate_max.field.verbose_name)
    memo = Field(attribute='memo', column_name=RunningRecord.memo.field.verbose_name)

    class Meta:
        model = RunningRecord
        fields = ('id', 'date', 'speed', 'pace', 'step_frequency', 'step_length',
                  'heart_rate_average', 'heart_rate_max', 'memo')
        export_order = ('date', 'speed', 'pace', 'step_frequency',
                        'step_length', 'heart_rate_average', 'heart_rate_max', 'memo')

