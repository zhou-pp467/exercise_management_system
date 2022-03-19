# by zhou_pp
from import_export import resources
from import_export.fields import Field
from plan.models import ExercisePlanItem, RunningPlanItem


class ExercisePlanResource(resources.ModelResource):
    date = Field(attribute='date', column_name=ExercisePlanItem.date.field.verbose_name)
    type = Field(attribute='type', column_name=ExercisePlanItem.type.field.verbose_name)
    memo = Field(attribute='memo', column_name=ExercisePlanItem.memo.field.verbose_name)

    class Meta:
        model = ExercisePlanItem
        fields = ('id', 'date', 'type', 'memo')
        export_order = ('date', 'type', 'memo')


class RunningPlanResource(resources.ModelResource):
    date = Field(attribute='date', column_name=RunningPlanItem.date.field.verbose_name)
    memo = Field(attribute='memo', column_name=RunningPlanItem.memo.field.verbose_name)

    class Meta:
        model = RunningPlanItem
        fields = ('id', 'date', 'memo')
        export_order = ('date', 'memo')