from django.http import HttpResponse, JsonResponse
import json
from serializers import StrengthRecordSerializer, RunningRecordSerializer,\
    ExercisePlanSerializer,RunningPlanSerializer
from exercise_type.models import StrengthTrainingRecord
from plan.models import ExercisePlanItem, RunningPlanItem
from running.models import RunningRecord
from rest_framework.decorators import api_view


@api_view(['GET'])
def get_day_data(request):
    try:
        year = request.GET.get('year')
        month = request.GET.get('month')
        date = f'{year}-{month}'
        running_records = RunningRecord.objects.filter(date__contains=date)
        strength_training_records = StrengthTrainingRecord.objects.filter(date__contains=date)
        exercise_plan_items = ExercisePlanItem.objects.filter(date__contains=date)
        running_plan_items = RunningPlanItem.objects.filter(date__contains=date)

        strength_records_serializer = StrengthRecordSerializer(strength_training_records, many=True)
        running_records_serializer = RunningRecordSerializer(running_records, many=True)
        exercise_plan_serializer = ExercisePlanSerializer(exercise_plan_items, many=True)
        running_plan_serializer = RunningPlanSerializer(running_plan_items, many=True)

        exercise_plan_items = [
            json.dumps({'id': f'{item["date"]}_{item["type"]}',
                        'start': f'{item["date"]} 00:00:00',
                        'end': f'{item["date"]} 23:59:59',
                        'title': item['type']
                        }) for item in exercise_plan_serializer.data
        ]
        exercise_record_items = [
            json.dumps({'id': f'{item["date"]}_{item["type"]}',
                        'start': f'{item["date"]} 00:00:00',
                        'end': f'{item["date"]} 23:59:59',
                        'title': item['type']
                        }) for item in strength_records_serializer.data
        ]
        running_record_items = list(set([
            json.dumps({'id': f'{item["date"]}_running',
                        'start': f'{item["date"]} 00:00:00',
                        'end': f'{item["date"]} 23:59:59',
                        'title': '跑步'
                        }) for item in running_records_serializer.data
        ]))
        running_plan_items = list(set([
            json.dumps({'id': f'{item["date"]}_running',
                        'start': f'{item["date"]} 00:00:00',
                        'end': f'{item["date"]} 23:59:59',
                        'title': '跑步'}
                       ) for item in running_plan_serializer.data
        ]))

        def merge_dict(dic1, dic2):
            dic1.update(dic2)
            return dic1

        exercise_plan_not_done_items = [merge_dict({'type': 'error'}, json.loads(item))
                                        if item not in exercise_record_items else
                                        None for item in exercise_plan_items]
        exercise_done_items = [merge_dict({'type': 'success'}, json.loads(item))
                               for item in exercise_record_items]
        running_plan_not_done_items = [merge_dict({'type': 'error'}, json.loads(item))
                                       if item not in running_record_items else None
                                       for item in running_plan_items]
        running_done_items = [merge_dict({'type': 'success'}, json.loads(item))
                              for item in running_record_items]

        result = exercise_plan_not_done_items + exercise_done_items + running_plan_not_done_items + running_done_items
        result = list(filter(lambda x: x is not None, result))

        res = JsonResponse({'businessCode': 1000, 'content': result})
        res['Access-Control-Allow-Origin'] = '*'
        return res
    except Exception as error:
        return HttpResponse(f'{error}')
