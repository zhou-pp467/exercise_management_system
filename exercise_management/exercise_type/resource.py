# by zhou_pp
from import_export import resources
from import_export.fields import Field
from exercise_type.models import StrengthTrainingRecord


class StrengthTrainingResource(resources.ModelResource):
    date = Field(attribute='date', column_name=StrengthTrainingRecord.date.field.verbose_name)
    type = Field(attribute='type', column_name=StrengthTrainingRecord.type.field.verbose_name)
    weight = Field(attribute='weight', column_name=StrengthTrainingRecord.weight.field.verbose_name)
    repeat_times = Field(attribute='repeat_times', column_name=StrengthTrainingRecord.repeat_times.field.verbose_name)
    memo = Field(attribute='memo', column_name=StrengthTrainingRecord.memo.field.verbose_name)

    class Meta:
        model = StrengthTrainingRecord
        fields = ('id', 'date', 'type', 'weight', 'repeat_times', 'memo')
        export_order = ('date', 'type', 'weight', 'repeat_times', 'memo')
