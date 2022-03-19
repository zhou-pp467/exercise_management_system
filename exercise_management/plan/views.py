# from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import json
import datetime
from serializers import StrengthRecordSerializer, RunningRecordSerializer,\
    ExercisePlanSerializer,RunningPlanSerializer
from exercise_type.models import StrengthTrainingRecord
from plan.models import ExercisePlanItem, RunningPlanItem
from running.models import RunningRecord
from rest_framework.decorators import api_view


@api_view(['GET'])
def get_calendar_data(request):
    try:
        start_date = datetime.datetime.strptime(request.GET.get('start_date'), '%Y-%m-%d')
        end_date = datetime.datetime.strptime(request.GET.get('end_date'), '%Y-%m-%d')
        running_records = RunningRecord.objects.filter(date__range=[start_date, end_date])
        strength_training_records = StrengthTrainingRecord.objects.filter(date__range=[start_date, end_date])
        exercise_plan_items = ExercisePlanItem.objects.filter(date__range=[start_date, end_date])
        running_plan_items = RunningPlanItem.objects.filter(date__range=[start_date, end_date])
    except Exception as error:
        print(str(error), '-------')
        raise RuntimeError
    strength_records_serializer = StrengthRecordSerializer(strength_training_records, many=True)
    running_records_serializer = RunningRecordSerializer(running_records, many=True)
    exercise_plan_serializer = ExercisePlanSerializer(exercise_plan_items, many=True)
    running_plan_serializer = RunningPlanSerializer(running_plan_items, many=True)

    return HttpResponse([{
        'strength_records': json.dumps(strength_records_serializer.data),
        'running_records': json.dumps(running_records_serializer.data),
        'exercise_plan': json.dumps(exercise_plan_serializer.data),
        'running_plan': json.dumps(running_plan_serializer.data)
    }])


@api_view(['GET'])
def get_day_data(request):
    try:
        date_str = request.GET.get('date')
        date = datetime.datetime.strptime(date_str, '%Y-%m-%d')
        running_records = RunningRecord.objects.filter(date=date)
        strength_training_records = StrengthTrainingRecord.objects.filter(date=date)
        exercise_plan_items = ExercisePlanItem.objects.filter(date=date)
        running_plan_items = RunningPlanItem.objects.filter(date=date)
    except Exception as error:
        raise RuntimeError
    strength_records_serializer = StrengthRecordSerializer(strength_training_records, many=True)
    running_records_serializer = RunningRecordSerializer(running_records, many=True)
    exercise_plan_serializer = ExercisePlanSerializer(exercise_plan_items, many=True)
    running_plan_serializer = RunningPlanSerializer(running_plan_items, many=True)
    exercise_items = list(set([i['type'] for i in strength_records_serializer.data] +
                              [i['type'] for i in exercise_plan_serializer.data]))
    # 只在plan里的项目type为error，其他情况type为success
    exercise_response = [{'date': date_str,
                          'type': 'error' if ((item in [i['type'] for i in exercise_plan_serializer.data]) and
                        (item not in [i['type'] for i in strength_records_serializer.data])) else 'success',
                          'content': item} for item in exercise_items]
    running_response = [{"date": date_str,
                        'type': 'success' if len(running_records_serializer.data) > 0 else 'error',
                         'content': '跑步'
                         }] if len(running_records_serializer.data) > 0 or len(running_plan_serializer.data) > 0 else []
    result = exercise_response + running_response

    return JsonResponse({'businessCode': 1000, 'content': result})
