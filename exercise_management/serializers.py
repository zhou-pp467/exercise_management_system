from rest_framework import serializers
from exercise_type.models import StrengthTrainingRecord
from plan.models import ExercisePlanItem, RunningPlanItem
from running.models import RunningRecord


# class StrengthTrainingTypeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = StrengthTrainingType
#         fields = '__all__'


class StrengthRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = StrengthTrainingRecord
        fields = '__all__'


class RunningRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = RunningRecord
        fields = '__all__'


class ExercisePlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExercisePlanItem
        fields = '__all__'


class RunningPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = RunningPlanItem
        fields = '__all__'
